#!/bin/bash

echo "Starting..." > /usr/src/app/log.txt

python3 /usr/src/app/scrape.py

echo "Done!" >> /usr/src/app/log.txt