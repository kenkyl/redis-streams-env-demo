import redis
import threading
import time
import random
from flask import Flask
from flask import request
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask import copy_current_request_context
from flask_cors import CORS
from db_service import RedisService


app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(app, cors_allowed_origins="*")

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
random.seed(1)


# new redis service setup
rHost = 'localhost'
rPort = 6379
redisService = RedisService(rHost, rPort)
redisService.test()
consumer_count = 0

# steams info setup
stream_name = 'stream'
streams_list = {
    stream_name: '$'
}
streams_list_group = {
    stream_name: '>'
}

# ENDPOINT /test
# GET - return the contents of redis INFO command to test health
@app.route('/test', methods = ['GET'])
def test_handler():
    redisService.test()
    info = redisService.get_info()
    print(f'redis info: {info}')
    return info

# ENDPOINT /test
# POST - add the contents of the request body to the redis stream
@app.route('/producers', methods = ['POST'])
def producers_handler():
    if(request.method == 'POST'):
        body = request.get_json()
        print(f'producer got body: {body}')
        # TODO REDIS SERVICE CALL - produce
        res = r.xadd(stream_name, body, id='*')
        print(f'result from producing: {res}')
        return res, 200
    else:
        return 'error: not found', 404

@socketio.on('createConsumer', namespace='/consumers')
def handle_event(json):
    @copy_current_request_context
    def consumer_thread_function(event_name):
        # streams setup
        consume = redisService.streams_consume(streams_list)
        # parse results
        listened = consume[len(consume)-1]
        samples = listened[len(listened)-1]
        id_latest, val_latest = samples[len(samples)-1]
        print(f'consumer RECEIVED: {id_latest} => {val_latest}')
        # emit consumed value via websocket to frontend to update
        # emit event with format <groupname><consumername>
        emit(event_name, val_latest)
        # recursivley call function to continue consuming
        consumer_thread_function(event_name)

    @copy_current_request_context
    def consumer_group_thread_function(group_name, consumer_name):
        # call redis service to group consume
        consume = redisService.streams_group_consume(group_name, consumer_name, streams_list_group)
        listened = consume[len(consume)-1]
        samples = listened[len(listened)-1]
        id_latest, val_latest = samples[len(samples)-1]
        print(f'consumer {consumer_name} in {group_name} RECEIVED: {id_latest} => {val_latest}')
        # emit consumed value via websocket to frontend to update
        # emit event with format <groupname><consumername>
        emit(consumer_name, val_latest)
        consumer_group_thread_function(group_name, consumer_name)

    @copy_current_request_context
    def consumer_init_thread(event_name, group_name):
        if (group_name is None):
            x = threading.Thread(target=consumer_thread_function, args=(event_name,))
        else:
            x = threading.Thread(target=consumer_group_thread_function, args=(group_name, event_name,))
        x.start()
        return 'started'

    print(f'received create consumer message: {json}')
    event_name = json.get('message')
    group_name = json.get('group')
    consumer_id = event_name[-1]
    data = { 'message' : event_name }

    # attempt to create the consumer group if needed
    if (group_name is not None):
        new_group = redisService.streams_new_consumer_group(stream_name, group_name)
        print(f'new consumer group {group_name} created: {new_group}')

    # start the thread to push updates for this consumer via websocks
    consumer_init_thread(event_name, group_name)
    # emit message via websocket to frontend to confirm registration of new consumer
    emit(f'createConsumer{consumer_id}', data)

@socketio.on('connect', namespace='/consumers')
def test_connect():
    print('consumers socket connected!')
    # emit('my-response', {'data': 'Connected'})


if __name__ == '__main__':
    sockeio.run(app)