#!/usr/bin/python3

#coding=utf-8
def xxx():
    return __name__
# 文件夹下面有__init__.py文件，那么这个文件夹就是一个包，包里面可以有多个模块
# 包：__init__.py可以为空，也可以有Python代码，因为__init__.py本身就是一个模块；也可以在__init__.py中导入包内的模块
# 模块: hello.py文件中定义了一个函数xxx，如果想在其他模块中使用hello.py中的函数，可以使用import语句引入hello.py模块
if __name__=="__main__":
    print(xxx())