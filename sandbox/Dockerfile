FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y python3.6 \
    && apt-get install -y gcc \
    && apt-get install -y g++ \
    && apt-get install -y default-jre \
    && apt-get install -y nodejs \
    && apt-get install -y curl

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y 
