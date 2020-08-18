#!/bin/bash
# get status
curl -o /dev/null --head --write-out '%{http_code}' "$1" -s
