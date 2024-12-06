FROM php:7.4-apache

COPY ./src /var/www/html/

COPY ./sct/docker-php.conf /etc/apache2/conf-enabled/docker-php.conf

COPY ./sct/flag /flag

RUN service apache2 restart