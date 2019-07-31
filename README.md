# klickr
Klickr is a simple photo sharing app. Think of a minuscule for Flickr.

The Klickr application has a webapp and a worker. Requires a postgres database and a redis server to work.

## How to Run

To run webapp:

    python run.py

To run the worker:

    ./worker.sh

## Running in Docker

Dockerfile is already part of the repo and docker image `pipalacademy/klickr` is available in Docker Hub.

To run the webapp:

    docker run -e DATABASE_URL=... -e... pipalacademy/klickr

To run the worker:

    docker run -e DATABASE_URL=... -e... pipalacademy/klickr ./worker.sh
