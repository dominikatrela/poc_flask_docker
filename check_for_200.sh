#!/bin/sh

GET_HTTP_CODE=$(curl -s -o /dev/null -w '%{http_code}' http://10.10.45.20:5000/test)

if echo ${GET_HTTP_CODE} | grep -q "200"; then
 echo 'you win !'
else
 echo 'oh no!'${GET_HTTP_CODE}
fi
