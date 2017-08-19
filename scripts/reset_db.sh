#!/bin/bash
# Script to reset the docker database.
docker exec -it bookingbot-sqlserver mysql -u root -ptoor booking -e "DROP TABLE IF EXISTS event,classroom,building"
