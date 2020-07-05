FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y python3.6 \
    && apt-get install -y gcc \
    && apt-get install -y g++ \
    && apt-get install -y default-jre \
    && apt-get install -y nodejs \
    && apt-get install -y curl \
    && apt-get install -y scala \
    && apt-get install -y wget \
    && apt-get install -y tar

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y 

RUN wget https://swift.org/builds/swift-5.2.4-release/ubuntu1804/swift-5.2.4-RELEASE/swift-5.2.4-RELEASE-ubuntu18.04.tar.gz \
    && tar xzf swift-5.2.4-RELEASE-ubuntu18.04.tar.gz \
    && mv swift-5.2.4-RELEASE-ubuntu18.04 ~
