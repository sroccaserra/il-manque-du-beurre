FROM debian:9

## Install Cron & other dependencies
RUN apt-get update && apt-get install --assume-yes python3 python3-pip python3-dev vim
RUN apt-get install --assume-yes curl

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY . /app

RUN pip3 install -e /app

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV FLASK_APP=/app/application.py FLASK_ENV=development
