#!/bin/sh

GET_HITS_1=$(curl -s /dev/null http://10.10.45.20:5000/test)
GET_HITS_2=$(curl -s /dev/null http://10.10.45.20:5000/test)

if expr $GET_HITS_2 - $GET_HITS_1 = 1; then
 echo 'you win !'
else
 echo 'oh no!'
fi