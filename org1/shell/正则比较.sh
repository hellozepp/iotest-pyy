#!/usr/bin/env bash
if [[ "1aaaaa1" =~ ^[0-9]+$ ]] #表示匹配纯数字
then
 echo "ok"
else
 echo "failed"
fi
#out : failed