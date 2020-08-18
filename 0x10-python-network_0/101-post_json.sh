#!/bin/bash
#check json
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1" -s
