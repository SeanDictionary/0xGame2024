FROM rust:1.79

COPY ./paste_bin/ /build/

WORKDIR /build/

RUN cargo build --release && \
    mkdir /app/ && \
    mv /build/target/release/paste_bin /app/ && \
    mv /build/db/ /app/ && \
    mv /build/public/ /app/ && \
    mv /build/static/ /app/ && \
    rm -rf /build/

WORKDIR /app/

CMD ["./paste_bin"]
