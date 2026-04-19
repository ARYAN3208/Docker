# Flask + Redis + Docker Compose Setup (README Notes)

## 📦 How Flask + Redis + Docker Compose Works

### Step-by-step working

1.  app2.py runs a Flask web server inside a container called **web**
2.  Redis runs inside another container called **redis**
3.  Docker Compose starts both containers together
4.  Docker Compose automatically creates a private network
5.  Flask connects to Redis using:

redis.Redis(host="redis", port=6379)

6.  Each time the webpage refreshes:
    -   Flask sends request to Redis
    -   Redis increases counter
    -   Flask shows updated visit number

Example output:

Hello! This page has been visited 1 times Hello! This page has been
visited 2 times

## ⚙️ What docker-compose.yml File Does

docker-compose.yml is a configuration file that tells Docker:

-   which containers to start
-   how to connect them
-   which ports to open
-   which images to use
-   startup order of services

It allows running multiple containers using one command:

docker compose up

## 📄 Explanation of docker-compose.yml

version: "3.9"

Defines Compose file version

services:

Defines containers to run

web:

Flask container name

build: .

Build image using current folder Dockerfile

ports: - "5000:5000"

Connects container port → local machine port

depends_on: - redis

Starts Redis before Flask

redis: image: redis:7

Downloads Redis container from Docker Hub

## 🌐 How containers communicate

Docker Compose automatically creates a network:

web ↔ redis

So Flask connects using:

host="redis"

instead of:

localhost

## 🚀 Commands used

Start containers:

docker compose up --build

Stop containers:

docker compose down

Open app:

http://localhost:5000

## ✅ What this project demonstrates

-   Running multiple containers together
-   Flask containerization
-   Redis integration
-   Container networking
-   Docker Compose basics
-   Multi-service backend setup (industry pattern)

## 📁 Project Folder Structure

project/

├── app2.py ├── requirements.txt ├── Dockerfile └── docker-compose.yml

## 🧩 app2.py Code

from flask import Flask import redis import time

app = Flask(**name**)

redis_client = redis.Redis(host="redis", port=6379)

@app.route("/") def home(): retries = 5 while True: try: count =
redis_client.incr("hits") return f"Hello! This page has been visited
{count} times." except redis.exceptions.ConnectionError: if retries ==
0: return "Redis connection failed." retries -= 1 time.sleep(1)

if **name** == "**main**": app.run(host="0.0.0.0", port=5000)

## 🧩 requirements.txt

flask redis

## 🧩 Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD \["python", "app2.py"\]

## 🧩 docker-compose.yml

version: "3.9"

services:

web: build: . ports: - "5000:5000" depends_on: - redis

redis: image: redis:7
