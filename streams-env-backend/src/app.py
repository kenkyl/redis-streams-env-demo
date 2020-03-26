import redis
import threading
import time
import random
from flask import Flask
from flask import request
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

r = redis.Redis(host = 'localhost', port = 6379, password = '')
random.seed(1)
stream_name = 'stream'

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

def thread_function(num):
    print(f'thread #{num} checking in...')
    time.sleep(5)
    thread_function(num)

@socketio.on('message', namespace='/test')
def handle_event(json):
    print(f'received json: {json}')
    data = { 'message': 'responding now!'}
    emit('event-response', data)

@socketio.on('connect', namespace='/test')
def test_connect():
    print('socket connected!')
    emit('my-response', {'data': 'Connected'})

if __name__ == '__main__':
    sockeio.run(app)