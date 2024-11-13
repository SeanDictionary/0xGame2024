FROM rust:1.79

COPY ./rogue_mysql/ /build/

WORKDIR /build/

RUN cargo build --release && \
    mkdir /app/ && \
    mv /build/target/release/rogue_mysql /app/ && \
    mv /build/public/ /app/ && \
    rm -rf /build/ && \
    echo "0xGame{rogue_mysql_file_read_c651e6a60def}" > /flag

WORKDIR /app/

CMD ["./rogue_mysql"]
