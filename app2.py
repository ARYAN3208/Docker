from flask import Flask
import redis
import time

app = Flask(__name__)

# connect to redis container
redis_client = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    retries = 5
    while True:
        try:
            count = redis_client.incr("hits")
            return f"Hello! This page has been visited {count} times."
        except redis.exceptions.ConnectionError:
            if retries == 0:
                return "Redis connection failed."
            retries -= 1
            time.sleep(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)