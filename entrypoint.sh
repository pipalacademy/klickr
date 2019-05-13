#! /bin/bash

set -e

sleep 10

# run the migrations
python migrate.py

# run the webapp
python run.py
