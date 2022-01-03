a="123123"
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
echo "paramter:"${dir}
# 1相对路径方式 /opt/projects/python/iotest-pyy/org1/shell/dirnameDemo/inner
cd "${base_dir}"
echo "相对路径方式:"
./inner/dirnameP.sh
# 2绝对路径方式 /opt/projects/python/iotest-pyy/org1/shell/dirnameDemo/inner
echo "绝对路径方式:"
${base_dir}/inner/dirnameP.sh
# 3bash命令调用 /opt/projects/python/iotest-pyy/org1/shell/dirnameDemo/inner
echo "bash命令调用:"
bash ${base_dir}/inner/dirnameP.sh
# 4 . (空格)  相对或绝对方式 /opt/projects/python/iotest-pyy/org1/shell/dirnameDemo
echo ". (空格):"
pname="parent"
. ${base_dir}/inner/dirnameP.sh
echo "pname:$pname"
echo ". (空格) 使用自己的shell路径:"
. ${base_dir}/inner/BASH_SOURCE.sh

#
#第一种和第二种没有什么区别，两种方式都需要提前赋予脚本以执行权限。
#
#第三种是把脚本当做bash的调用来处理，所以，脚本不需要有执行权限就可以执行。
#
#前三种方式都是在当前shell中打开一个子shell来执行脚本内容，当脚本内容结束，则子shell关闭，回到父shell中。
#
#第四种是使脚本内容在当前shell里执行，而不是单独开子shell执行。