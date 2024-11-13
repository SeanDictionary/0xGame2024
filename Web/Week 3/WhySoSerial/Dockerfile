FROM golang:1.22 AS builder

COPY ./src/readflag.go /build/

WORKDIR /build/

RUN go build -o readflag readflag.go

FROM openjdk:8

COPY --from=builder --chmod=755 /build/readflag /

COPY ./src/WhySoSerial.jar /app/

WORKDIR /app/

RUN groupadd -r user && \
    useradd -m -r -g user user && \
    chown -R root:root /app/ && \
    chmod -R 755 /app/

RUN echo '0xGame{easy_ysoserial_commonscollections_05c68d08abf2}' > /flag && \
    chmod 400 /flag && \
    chmod 4755 /readflag

USER user

CMD ["java", "-jar", "/app/WhySoSerial.jar"]
