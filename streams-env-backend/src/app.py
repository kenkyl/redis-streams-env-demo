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

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
random.seed(1)
stream_name = 'stream'

# TODO - update the $ to > for XREADGROUP
streams_list = {
    stream_name: '$'
}

@app.route('/producers', methods = ['POST'])
def producers_handler():
    if(request.method == 'POST'):
        body = request.get_json()
        print(f'got body: {body}')
        res = r.xadd(stream_name, body, id='*')
        print(f'result from producing: {res}')
        return res, 200
    else:
        return 'error: not found', 404

@app.route('/threads', methods = ['POST'])
def theads_test():
    num = random.randint(0, 100)
    x = threading.Thread(target=thread_function, args=(num,))
    x.start()
    return 'started', 200

@socketio.on('message', namespace='/test')
def handle_event(json):
    print(f'received json: {json}')
    data = { 'message': 'responding now!'}
    emit('event-response', data)

@socketio.on('connect', namespace='/test')
def test_connect():
    print('socket connected!')
    emit('my-response', {'data': 'Connected'})

# @socketio.on('message', namespace='/consumers')
# def handle_event(json):
#     print(f'received json: {json}')
#     data = { 'message': 'responding now!'}
#     emit('event-response', data)

@socketio.on('createConsumer', namespace='/consumers')
def handle_event(json):
    @copy_current_request_context
    def consumer_thread_function(event_name):
        # streams setup
        consume = r.xread(streams_list, block=0)
        # parse results
        listened = consume[len(consume)-1]
        samples = listened[len(listened)-1]
        id_latest, val_latest = samples[len(samples)-1]
        print(f'consumer # {event_name} RECEIVED: {id_latest} => {val_latest}')
        emit(event_name, val_latest)
        consumer_thread_function(event_name)

        # random.seed(time.localtime)
        # num = random.randint(0, 100)
        # message = f'{event_name} checking in with #{num}'
        # print(message)
        # emit(event_name, message)
        # time.sleep(5)
        # consumer_thread_function(event_name)

    @copy_current_request_context
    def consumer_init_thread(event_name):
        x = threading.Thread(target=consumer_thread_function, args=(event_name,))
        x.start()
        return 'started', 200

    print(f'received create consumer message: {json}')
    event_name = json.get('message')
    consumer_id = event_name[-1]
    data = { 'message' : event_name }
    consumer_init_thread(event_name)
    emit(f'createConsumer{consumer_id}', data)

@socketio.on('connect', namespace='/consumers')
def test_connect():
    print('consumers socket connected!')
    # emit('my-response', {'data': 'Connected'})


if __name__ == '__main__':
    sockeio.run(app)