#!/bin/bash

firstname=$1
lastname=$2
show=$3

if [ "$show" = "true" ]; then
    echo "Hello $firstname $lastname"
else
    echo "The option chosen was to not show the message..."
fi


