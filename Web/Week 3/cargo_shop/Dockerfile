FROM rust:1.79

COPY ./cargo_shop/ /app/

WORKDIR /app/

RUN cargo install --path . && \
    cargo clean

CMD ["cargo_shop"]
