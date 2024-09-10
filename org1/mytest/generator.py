print(type(range(10)))
# ① 所有的生成器都是迭代器.
# ② 迭代器(iterator)用类实现, 生成器(generator)用函数实现

# iterator
# Python 中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法，那么它就是一个可
# 迭代对象(如: tuple, list, dict)

# generator
# 生成器可以认为是一个简化版的迭代器, 生成器的实现是基于函数.再函数中使用关键字“yield” 而不是通常用的return.yield作为生成器执行的
# 暂停恢复点, 每次调用next, 生成器函数执行到yield语句, 会挂起, 并保存当前的上下文信息.知道下一个next触发生成器继续执行.

# generator 和 iterator 的区别有 2 点：
# 1. generator 使用 yield 语句，而 iterator 使用 __iter__ 和 __next__ 方法
# 2. generator 会在每次调用 next() 时执行，而 iterator 会在初始化时执行
# 平方表
square_table = []
for i in range(5000):
    square_table.append(i * i)
for i in range(5):
    print(square_table[i])
    
square_generator = (x * x for x in range(50000))
print(type(square_generator))
for i in range(5):
    print(next(square_generator))

def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1

import traceback
f = fib(5)
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print("『==========』")
try:
    print(next(f))
except StopIteration:
    traceback.print_exc()
for i in fib(5):
    print(i)
