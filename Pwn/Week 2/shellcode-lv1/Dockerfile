FROM ubuntu:focal-20240530

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/http:\/\/security.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y xinetd

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /usr/lib* /home/ctf && \
    mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /bin/base64 /home/ctf/bin

RUN mkdir /home/ctf/dev/  && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

COPY build/flag /home/ctf/flag
COPY build/xinetd.conf /etc/xinetd.d/ctf
COPY build/init.sh /init.sh
COPY dist/pwn /home/ctf/pwn

RUN chown root:root /etc/xinetd.d/ctf && \
    chown root:root /init.sh && \
    chmod 400 /etc/xinetd.d/ctf && \
    chmod 500 /init.sh && \
    chown -R ctf:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/init.sh"]

EXPOSE 9999