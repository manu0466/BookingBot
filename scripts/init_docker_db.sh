#!/bin/bash
# Script to initialize a docker container for the bot

docker run \
--name bookingbot-sqlserver \
-v $PWD/botdb:/var/lib/mysql \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=toor \
-e MYSQL_USER=booking-bot \
-e MYSQL_PASSWORD=botpassword \
-e MYSQL_DATABASE=booking \
-d mysql/mysql-server:latest