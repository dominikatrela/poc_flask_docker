from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'costam costam :){}'.format(count)

@app.route('/test')
def licz():
    count = redis.incr('hits')
    return str(count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)