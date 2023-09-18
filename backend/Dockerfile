# dev python because https://memgraph.github.io/pymgclient/introduction.html#build-prerequisites
FROM kuralabs/python3-dev:latest

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN apt-get update
RUN apt install -y cmake make gcc g++ libssl-dev

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
