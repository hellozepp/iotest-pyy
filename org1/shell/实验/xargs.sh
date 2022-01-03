#!/usr/bin/env bash
function rand(){
  min=$1
  max=$(($2-$min+1))
  num=$(($RANDOM+1000000000)) #增加一个10位的数再求余
  echo $(($num%$max+$min))
}
fun1(){
  echo $1 start
  sleep $(rand 1 10)s
  echo $1 end
}
export -f fun1
export -f rand
#cat `pwd`/xargs.txt | xargs -P 10 -i bash -c "fun1 {}"
#echo a.b | xargs -P 1 -i bash -c "fun1 {}"
echo a.b | xargs  -i bash -c "echo $@"

