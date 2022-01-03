#!/bin/bash
#数组

#定义数组
array_name=(1 2 3 4)
array_name[0]=5

echo ${array_name[0]}
#使用@符号可以获取数组中的所有元素
echo ${array_name[@]}

#取得数组元素的个数
echo ${#array_name[@]}
echo ${#array_name[*]}
# 取得数组单个元素的长度
str=("abc" "defgh")
echo $str #abc
echo ${#str[0]}
echo ${#str[1]}
echo "-------------------------"
arr=("tuple1" 2 "3")
echo "Elements in arr1: ${arr[@]}"
i=0
unset "arr[$i]"
echo "Length of arr1: ${#arr[@]}"
echo ${arr[*]}
echo ${arr[0]}
let "arr[1]-=1"
echo ${arr[1]}
echo ${arr[2]}
arr+=(3 5)
echo "Elements in arr1: ${arr[@]}"

j=0
for i in ${arr[@]};do
if [ $i -eq 3 ];then
echo 'unset arr[$j] $j:'$j
unset "arr[$j]"
fi
let "j+=1"
done

j=0
echo '${#arr[@]}:'"${#arr[@]}"
for i in ${arr[@]};do
echo "-- $j:$i --"
let "j+=1"
done

unset arr
echo 'unset $arr'
echo ${arr[0]}
count=0
let "count+=1"
max_threshold=1
echo "$count $max_threshold"
if [[ ${count} -le ${max_threshold} ]];then
echo "hehe"
fi