# syntax=docker/dockerfile:1
FROM python:3.9-alpine

RUN apk add --no-cache git
WORKDIR /app

RUN git clone https://github.com/davbrican/InnoBuddy.git 
WORKDIR /app/InnoBuddy

RUN pip install -r ./requirements.txt

ENTRYPOINT python ./src/main.py && /bin/bash
