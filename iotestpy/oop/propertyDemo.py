class Student:
    def __init__(self):
        self._age = None
        self.__name = '张三'
        self._location = '山东'
        self._data = {"k": "v"}

    @property
    def age(self):
        print(f'获取属性 {self._age} 时执行的代码')
        return self._age

    @age.setter
    def age(self, age):
        print(f'设置属性 {age} 时执行的代码')
        self._age = age

    @age.deleter
    def age(self):
        print(f'删除属性 {self._age} 时执行的代码')
        del self._age

    @property
    def data(self):
        print(f'获取属性 {self._data} 时执行的代码')
        return self._data

    @data.deleter
    def data(self):
        print(f'删除属性 {self._data} 时执行的代码')
        del self._data


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
data_ = student.data
# 删除引用变量. 由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。
del data_ # 解除 data_ 对数据对象的引用，此时数据对象的引用计数为1
print("data:", student.data)
del student.data
# print("data:", student.data) # 'Student' object has no attribute '_data'
"""
删除属性时执行的代码
"""
