#!/bin/bash
#catch the line
curl -X PUT 0.0.0.0:5000/catch_me > /dev/null
curl -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me_2 > /dev/null
curl -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me_3
