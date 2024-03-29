#!/bin/bash
set -u
set -e
set -o pipefail
#流程控制-----循环--while
#./10.sh 1 2 3 4

sum=0
i=1
while ((i <= 10)); do
  let "sum+=i"
  let "i += 2"
done

echo "sum=$sum"

#===========================================
echo "Please input the num(1-10) "
read num

while [[ "$num" != 4 ]]; do #不是数字报错
  if [ "$num" -lt 4 ]; then
    echo "Too small. Try again!"
    read num
  elif [ "$num" -gt 4 ]; then
    echo "To high. Try again"
    read num
  else
    exit 0
  fi
done

echo "Congratulation, you are right! "

#===============================================
echo "number of arguments is $#"

echo "What you input is: "

while [[ "$*" != "" ]]; do
  echo "$1"
  shift
done
echo $0 #路径名
echo "生成连续数组系列："
a=($(seq 1 3 10))
echo ${a[1]}
echo ${a[@]}

#-------------
lib_path=/opt/projects/kyligence/kolo-build/dev/lib
echo "Downloading Spark 3.1.1" &&
  cd "${lib_path}" &&
  times_tried=0
while [ $times_tried -le 3 ]; do
  echo "Downloading $times_tried"
  # 注意：if里面的异常不会被set -e中断
#  if curl -O https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz && tar -zxvf spark-3.1.1-bin-hadoop3.21.tgz; then
  if true && tar -zxvf spark-3.1.1-bin-hadoop3.21.tgz; then
    break
  fi
  if [[ $times_tried -ge 3 ]];then
    echo "download failed!"
    exit 1;
  fi
  times_tried=$((times_tried + 1))
  rm -rf spark-3.1.1-bin-hadoop3.2.tgz
done
