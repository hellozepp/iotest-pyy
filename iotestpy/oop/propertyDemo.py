class Student:
    def __init__(self):
        self._age = None
        self.__name = '张三'
        self._location = '山东'

    @property
    def age(self):
        print('获取属性时执行的代码')
        return self._age

    @age.setter
    def age(self, age):
        print('设置属性时执行的代码')
        self._age = age

    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age


student = Student()

# 设置属性
student.age = 18
"""
设置属性时执行的代码
"""

# 获取属性
print('学生年龄为：' + str(student.age))
print('学生姓名为：' + student._Student__name)  # 强制访问私有属性
print('学生为：' + student._location)  # 强制访问私有属性
"""
获取属性时执行的代码
学生年龄为：18
_xxx 不能用’from module import *’导入

__xxx__ 系统定义名字

__xxx 类中的私有变量名

对 __init__() 方法的调用发生在实例被创建之后 。如果要控制实际创建进程，请使用 __new__() 方法。
按照约定， __repr__() 方法所返回的字符串为合法的 Python 表达式。
在调用 print(x) 的同时也调用了 __str__() 方法。
由于 bytes 类型的引入而从 Python 3 开始出现。

"""

# 删除属性
del student.age
"""
删除属性时执行的代码
"""
