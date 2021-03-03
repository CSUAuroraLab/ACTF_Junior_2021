FROM mattrayner/lamp:latest-1804

COPY ./index.php /var/www/html/index.php

RUN rm -rf /var/www/phpmyadmin && \
	rm -rf /var/www/phpMyAdmin-5.0.2-all-languages

EXPOSE 80

