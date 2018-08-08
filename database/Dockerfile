FROM postgres:10

RUN apt-get update && \
    apt-get install --assume-yes \
    libpq-dev netcat python3 python3-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY ./scripts/create_databases.sh /docker-entrypoint-initdb.d/create_databases.sh
COPY . /app
