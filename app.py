from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis. We use the hostname 'redis' which we will define later in Docker Compose
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello! I have been seen {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


