#!/bin/bash
#变量和引用--本地变量

#对变量赋值：
a="hello world"
# 现在打印变量a的内容：
echo "A is:"
echo $a             #echo ${a}与之结果相同
echo ${a}

#${str:a:b} 表示提取字符串a开始的b个字符
#比如
str="abcd"
echo ${str:0:3}
#结果是abc

#set -- #后无内容，将当前 shell 脚本的参数置空，$1 $? $@ 等都为空。
#set -- #后有内容，当前 shell 脚本的参数被替换为 set -- 后的内容，$1 $? $@ 等相应地被改变。
set -- aa ss dd
#set -- mysqld "$@

#linux中的set命令: "set -e" 与 "set -o pipefail"
#在"set -e"之后出现的代码，一旦出现了返回值非零，整个脚本就会立即退出。有的人喜欢使用这个参数，是出于保证代码安全性的考虑。但有的时候，这种美好的初衷，也会导致严重的问题。
#设置了这个选项以后，包含管道命令的语句的返回值，会变成最后一个返回非零的管道命令的返回值。即管道语句里面任何一个非零即非零
#================================================

#使用花括号避免变量名与其他文字混淆
num=2
echo "this is the $numnd"
echo "this is the ${num}nd" #注意括号的位置
echo 'this is the ${num}nd'


#================================================
echo "=================数学运算==============="
#let表示数学运算
#expr用于整数值运算，每一项用空格隔开
#$[]将中括号内的表达式作为数学运算先计算结果再输出。

var=1
var=$var+1
echo $var

var=1
let "var+=1"
echo $var

var=1
echo $[ 1 == 2 ] #res:0  1
var=$[ $var + 1 ]
echo $var
if [$1 == ""];
then
echo "none1"
else
echo "123"
fi
echo '-------expr--------'
var=1  
var=`expr $var + 1.5`     #注意加号两边的空格，否则还是按照字符串的方式赋值。not a decimal number: '1.5'
echo $var # syntax error

var=1  
var=`expr $var+ 1` # 跟$()效果一致
echo $var
echo 'echo $var 1' $var 1

#==============================================
#显示本地变量
#set
#清除本地变量
echo '清除本地变量'
unset var
echo $var

