#! /bin/bash

if [ -z $REDIS_URL ]; then
    REDIS_URL=redis://
fi

rq worker klickr --url $REDIS_URL
