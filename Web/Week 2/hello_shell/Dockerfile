FROM php:7.4-apache

COPY ./src /var/www/html/

COPY ./sct/flag /flag

COPY ./sct/readME /readME

RUN chmod 600 /flag && install -m =xs $(which wc) .