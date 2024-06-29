# 测试该脚本：
#变量和引用--位置变量&特殊变量

#位置变量：$0,$1,$2,$3……$9
echo "Number of parameters is" $# #获取参数个数，没有是0
echo "bash name is" $0
echo "Program 1 name is" $1
echo "Parameters as a single string is" $*

#===========================================
echo 1 $@  #所有脚本的命令行参数，它们分别被双引号引住，如"$1"  "$2"  “$3” ...例如可以用在for循环中的in后面。$*类似
echo 2 $$  #脚本运行的当前进程ID号
echo 3 $!  #后台运行的最后一个进程的ID号
echo 4 $?  #显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。

cd /
echo $0 #Shell本身的文件名
echo 'echo $(dirname $0):' $(dirname $0) # 返回当前绝对路径
echo "current path is :"
"pwd"
echo "============================="
DIR="$(cd "$(dirname "$0")" && pwd)" # 切换到脚本所在的目录，并返回路径
echo "进入当前脚本的地址，获取脚本的所在路径:" $DIR

echo $@和$*在\"\"下区别是@是每一个参数 *作为一个参数
for i in $@
do
echo "${i}"
done

## shift接受一个数字作为参数，然后把所有的位置参数向左移动这个数字的位数（即删掉前几个）。如果shift后面不跟数字，那么默认的数字是1
shift
echo "shift it！" $@
echo ===================================
for i in $* #=> "1 1 1 1"
do
echo ${i}
done
for i in $@ #=> "1 1 1 1"
do
echo ${i}
done


