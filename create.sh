#!/bin/bash
# Probably want to re-code this into node or python at some point
# Maybe pad the day numbers so Day6 -> Day06?
set -x
if [[ $# -lt 2 ]]; then
    echo "Usage: ./create.sh <year> <day>"
    exit 1
fi

re='^[0-9]+$'
if ! [[ $1 =~ $re ]]; then
    echo "Year must be number."
    exit 1
fi
if ! [[ $2 =~ $re ]]; then
    echo "Day must be number."
    exit 1
fi

cp -r Template $1/Day$2
cd $1/Day$2