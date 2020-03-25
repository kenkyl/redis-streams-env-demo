import redis
from flask import Flask
from flask import request

app = Flask(__name__)

r = redis.Redis(host = 'localhost', port = 6379, password = '')

stream_name = 'stream'

@app.route('/producers', methods = ['POST'])
def producers_handler():
    if(request.method == 'POST'):
        body = request.get_json
        print("Adding to stream %s" % body)
        #r.xadd(stream_name, body, id='*')
    return 'DONE'