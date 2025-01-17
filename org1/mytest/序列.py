# coding=utf-8
from collections import OrderedDict
print("=======dict========")
# 字典、set, 可以看见，遍历一个普通字典
my_dict = dict()
my_dict["name"] = "zhangsan"
my_dict["age"] = 18
my_dict["girl"] = "Tailand"
my_dict["money"] = 80
my_dict["hourse"] = None

for key, value in my_dict.items():
    print(key, value)
print("------OrderedDict------")
my_dict = OrderedDict()
my_dict["name"] = "zhangsan"
my_dict["age"] = 18
my_dict["girl"] = "Tailand"
my_dict["money"] = 80
my_dict["hourse"] = None

for key, value in my_dict.items():
    print(key, value)
print("-----整体打印-------")
zidian1 = {"1": 1, "a": 3, "1": 1, 3: 1, 2: 1, "b": "b", "test": [1]}
print(zidian1)
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # 输出: dict_keys(['a', 'b', 'c'])
# 取单个值
print("-----取单个值-------")
print(zidian1["1"])
# print(zidian1[1]) #KeyError: 1
print("-----修改单个值-------")
zidian1["1"] = zidian1["1"] + 5
print(zidian1["1"])
# 判断key是否存在
print("-----判断key是否存在-------")
print("1" in zidian1)  # {'1': 6, 'a': 2, 3: 1, 2: 1, 'b': 'b'}
print(1 in zidian1)
print("-----修改引用-------")
tmpList = zidian1.get("test")
tmpList[0] = 10
print(zidian1)


def a(str):
    pass


a1 = a("1")
a2 = a("2")
zidian1["a1"] = a1

# 删除
del (zidian1["1"])
print("1遍历")
# 遍历
for t in zidian1:
    print("key:", t, "value:", zidian1[t])
# 2
print("1遍历2")
for k, v in list(zidian1.items()):
    print((k, v))

print("追加----")
zidian1["a"] = "b"  # 会覆盖以前的value
print(zidian1)

if not zidian1.get("asdf"):
    print("hehe")
else:
    print("you")
print("size========")
print(len(zidian1))
print("=======list========")
li = list(range(10))
print(li)
liebiao = [1, "a", 2, 2, 2, 2, {1: 2}]
# 删除
del liebiao[-1]  # 根据索引删除
print(liebiao)  # <class 'list'>: [1, 'a', 2, 2, 2, 2]
tmp = liebiao[1]
liebiao.remove("a")  # 根据值删除 <class 'list'>: [2, 2, 2, 2]
print(tmp)
# liebiao.remove("a") #闪不存在的报错
liebiao = list(range(0, 10))
print(liebiao)
liebiao.remove(1)
print(liebiao)
print("2遍历")
# 遍历
for key in liebiao:
    print(key)
print("追加----")
liebiao.append("new")
print(liebiao)
liebiao.extend(["心列表", 1])  # addAll
print("%r" % liebiao)  # <class 'list'>: [0, 2, 3, 4, 5, 6, 7, 8, 9, 'new', '心列表', 1]
# liebiao.extend(1) #TypeError: 'int' object is not iterable
print("%r" % "123\n")  # 格式化输出
print("%s" % "123\n")  # 字符串输出
print(str(liebiao))
liebiao += ["aaaaaaa"]
print(liebiao)
print(liebiao[-1])
# 判空
list = [[]]
if list:
    print("pass")
else:
    print("list is null!!!!")
# contains
list = [1, 2, a1]
print(a2 in list)

print("=======判断 list = [] 是否是false========")
list = []
print(len(list))
if not list:
    print("list is null")
else:
    print("list is not null")
# list = None
# print(len(list)) #error

print("=======list进行浅拷贝========")
list = [1, 2, 3, 4, 5]
list1 = list.copy()
list.clear()
print(list1)

print("=======list进行深拷贝========")
list = [1, 2, 3, 4, 5]
import copy

list1 = copy.deepcopy(list)
list.clear()
print(list1)
print("=======tuple是只读序列========")
# tuple是只读序列
tuple = ("这是", "只读", zidian1)
zidian1[3] = 'TAINJIA'
print("zidian1修改后：", zidian1)
print("tuple修改后：", tuple)
print("tuple[0]:" + tuple[0])
print("3遍历")
# 遍历
for t in tuple:
    print(t)

li = [i * 3 for i in range(10)]
print(li)
print("range建list   做深拷贝")
li_2d = [[i] * 3 for i in range(3)]
print(li_2d)  # 二维数组
li_2d[0][0] = 3
print(li_2d)

print("=======set========")
# set没有重复原宿
s_a = {1, 2, 3, 4, 5, 6}
s_b = set([4, 5, 6, 7, 8, 9])
print(s_a)
print(s_b)

# 判断元素是否存在
print((5 in s_a))
print((10 in s_b))

# 并集
print((s_a | s_b))
print((s_a.union(s_b)))

# 交集
print((s_a & s_b))
print((s_a.intersection(s_b)))

# 差集 A - (A & B) 保留左边
#      b - a 保留右边
print((s_a - s_b))  # {1, 2, 3}
print((s_a.difference(s_b)))  # {1, 2, 3}
print((s_b - s_a))  # 7, 8, 9

# 对称差 (A | B) - (A & B)
print((s_a ^ s_b))  # {1, 2, 3, 7, 8, 9}
print((s_a.symmetric_difference(s_b)))

# 修改元素
s_a.add('x')
s_a.update([4, 5, 60, 70])  # 在s中添加多项
print(s_a)

s_a.remove(70)
print(s_a)
# s_a.remove(100)
for i in s_a:
    print(i)

# 生成器
print("-----------------生成器----------------")
square_generator = (x * x for x in range(10000))
for i in range(10):
    print((next(square_generator)))
print("---------------------------------")


def two_sum(num, target):
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]
    return [-1, -1]


ret = two_sum([2, 7, 11, 15], 18)
print((type(ret)))
print((two_sum([2, 7, 11, 15], 18)))
print((two_sum([2, 7, 11, 15], 30)))

# 3.5从中间生成
# def fib(limit):
#     n, a, b = 0, 0, 1
#     while n < limit:
#         yield b
#         a, b = b, a + b
#         n += 1
#     return 'done'
#
# import traceback
# f = fib(5)
# print(type(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# try:
#     print(next(f))
# except StopIteration:
#     traceback.print_exc()
# for i in fib(5):
#     print(i)
print("===========列表三种追加===============")
'''
 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。

1.list+list
2.  append() 方法向列表的尾部         添加一个新的元素        。只接受一个参数。

3.  extend()方法只                 接受一个列表      作为参数，并将该参数的每个元素都添加到原有的列表中。
'''
# 1 相加
list1 = [1, "2", "a"]
list2 = [6, ]
list1 = list1 + list2  # 相当于 extend
print(list1)  # [1, '2', 'a', 6]
list2 = [5, 3]
list1 = list1 + list2
print(list1)  # [1, '2', 'a', 6]
# 2 extend
list1 = [1, 2, 3]
list2 = [3, 5, 6]
list1.extend(list2)
print(list1)
print(list1[1])  # 2
list1.extend("aaa")  # 自动转化成列表
# [1, 2, 3, 3, 5, 6, 'a', 'a', 'a']
list1.extend([1, 2])
# list1.extend(1)#TypeError: 'int' object is not iterable
# list1.extend(-1.35) #TypeError: 'float' object is not iterable
# list1.extend(134)#TypeError: 'int' object is not iterable
print(list1)

# 3 append
print(list1.append(1))
print(list1)
list1.append([1, 2, 3])  # 追加作为一个元素
print(list1)
# list1.append(1,2) #不支持多个数
# print list1
print("=======set========")

s = set([3, 5, 9, 10])  # 创建一个数值集合
t = set("Hello")  # 创建一个唯一字符的集合
a = t | s  # t 和 s的并集
b = t & s  # t 和 s的交集
c = t - s  # 求差集（项在t中，但不在s中）
d = t ^ s  # 对称差集（项在t或s中，但不会同时出现在二者中）
print(a, b, c, d)
print("\n")
s.update([1, 2, 4, 6, 7, 8])
print(s)
print("==========有序 OrderedDict===============")
# 使用键值对列表初始化有序字典
od = OrderedDict([('b', 1), ('c', 2), ('d', 3)])
# 添加元素
od['a'] = 4
od = OrderedDict(sorted(od.items(), key=lambda t: t[0]))

# 访问元素
print(od['a'])  # 输出: 1

print(od)
