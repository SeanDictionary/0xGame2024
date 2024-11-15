FROM ubuntu:20.04

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev ncat
RUN adduser --disabled-password --gecos '' test
RUN chmod 666 /etc/passwd

WORKDIR /app

COPY . /app

RUN chmod 755 /app
RUN chmod 111 ./Dockerfile
RUN chmod 777 ./wrapper.sh
RUN chmod 400 ./flag

USER test

CMD ncat -klvp 2000 -m 999999 -e ./wrapper.sh
