FROM mattrayner/lamp:latest-1804

COPY ./index.php /var/www/html/index.php
COPY ./index.html /var/www/html/index.html
COPY ./flag.txt /flag.txt
COPY ./rmUploadFiles.sh /rmUploadFiles.sh
COPY ./run.sh /run.sh
RUN rm -rf /var/www/phpmyadmin && \
	rm -rf /var/www/phpMyAdmin-5.0.2-all-languages && \
    chmod +x /rmUploadFiles.sh && \
    chmod +x /run.sh && \
	chown root:www-data /app && \
	mkdir -p /app/upload && \
	chown www-data:www-data /app/upload

EXPOSE 80

CMD /run.sh
