FROM node

COPY ./next-db/ /app/

WORKDIR /app/

RUN npm install && \
    npm run build

CMD ["./run.sh"]
