#!/usr/bin/env bash

test='c:/windows/boot.ini'
echo ${test#/}  
#c:/windows/boot.ini  
echo ${test#*/}  
#windows/boot.ini  
echo ${test##*/}  
#boot.ini  
  
echo ${test%/*} 
#c:/windows 
echo ${test%%/*} 
#c:
#${变量名#substring正则表达式}从字符串开头开始配备substring,删除匹配上的表达式。 
#${变量名%substring正则表达式}从字符串结尾开始配备substring,删除匹配上的表达式。 
#注意：${test##*/},${test%/*} 分别是得到文件名，或者目录地址最简单方法。   

echo 1 ${0}
echo 2 ${0#*/} # #删除左边到截断处 X
echo 3 ${0##*/} #右边开始遍历，到/处  #3 截断.sh 贪婪匹配
echo 4 ${0%/*} # %右边遍历，到/处
echo 5 ${0%%/*} #删除全部，匹配左边/* 找到了/opt/projects/python/iotest-py/shell/1.shell变量/截断.sh X
#1 /opt/projects/python/iotest-pyy/org1/shell/1.shell变量/截断.sh
#2 opt/projects/python/iotest-pyy/org1/shell/1.shell变量/截断.sh
#3 截断.sh
#4 /opt/projects/python/iotest-pyy/org1/shell/1.shell变量
#5
