#!/bin/bash
#URL passed as an argument, and displays only the status code of the response
curl -o /dev-head --write-out '%{http_code}' "$1"
