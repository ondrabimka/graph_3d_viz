FROM python:3.10

WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

COPY . .
