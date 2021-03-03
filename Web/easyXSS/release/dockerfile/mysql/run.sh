#!/bin/bash

echo "#################  init xss-mysql start  ##################"
echo "1. Starting the mysql service"
mysqld --user=root &
echo "   Wait for 10 seconds till mysql service started..."
sleep 10
echo "2. exec /tmp/board.sql"
mysql -uroot -proot < /tmp/board.sql
echo "#################  init xss-mysql stop   ##################"
tail -f /dev/null
