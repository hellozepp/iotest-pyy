# coding=utf-8
import random
from datetime import date

from numpy import float32, float64

intv = 1
floatv = 1.1
strv = "19"
strv2 = "19.9"

print(bin(10))
print(oct(10))
print(hex(10))

print(random.randint(20, 50))  # 生成20-50之间的随机数 20 <= n <= 50
# =====================================================
print("=========================float===========================")
d1 = 0.1
d2 = 0.2
print(d1 + d2)

# 创建单精度浮点数
single_precision_number = float32(123.456)
print(single_precision_number)
single_precision_number = float32(1.2000000476837158)
print(single_precision_number)
# 创建双精度浮点数
double_precision_number = float64(789.123456789)
print(double_precision_number)

from decimal import Decimal

d3 = Decimal('0.1') / Decimal('0.3')
print(d3)

from decimal import getcontext

getcontext().prec = 4  # 设置全局精度
d3 = Decimal(0.1) / Decimal(0.3)
print(d3)
print(d1 + d2)

from fractions import Fraction

d4 = Fraction(16, -10)  # 分子分母
print(d4)
print(str(d4._numerator) + "\t" + str(d4._denominator))
print(Decimal(d4._numerator) / Decimal(d4._denominator))

d5 = divmod(10, 3)
print(str(d5[0]) + "\t" + str(d5[1]))

# =====================================================
print("========================2============================")
inta = int(strv)
floata = float(strv2)
stra = str(intv) + "aaa"

print(inta + 1)
print(floata + 0.1)
print(stra)

print(type(inta))
print(isinstance(inta, int))

a = b = c = 2

a, b, c = 1, 2, "aaa"

d = 4 + 4j  # 复数

del a
# print(a)
# =====================================================
print("=========================3===========================")
print(2 / 4)
print(2 // 4)  # 整除
print(2 ** 4)  # 2的4次方

strv3 = "Runoob"
print(strv3[0:-1])
print(strv3[0])
print(strv3[0:10])
print(strv3 * 2)
print(len(strv3))
print(strv3[0:len(strv3)])

# =====================================================
print("===========================4=========================")

mylist = [1, 2, True, "aaa"]
mylist2 = ["a", "b"]
mylist3 = [1, ]
print(mylist[2])

mylist[2] = "aaaa"
mylist.append("xxx")

print(mylist[2])
print(mylist[0:])
print(mylist[1:2])
print(mylist * 2)
print(mylist + mylist2 + mylist3)
mylist[0:2] = []
print(mylist)
mylist.remove("xxx")
print(mylist)
print(mylist.__len__())
# []to string
print("*".join(mylist))

# =====================================================
print("=========================5===========================")

mytuple = (1, "小明", "男", 25)
mytuple2 = (2, "小华", "男", 1)
tup = (1,)
print(mytuple)
print(mytuple2)
(id, name, sex, age) = mytuple
print(str(id) + " " + name + " " + sex + " " + str(age))
print(mytuple[2])
print(mytuple[0:])
print(mytuple[1:2])
print(mytuple * 2)
print(mytuple + mytuple2)
# mytuple[0:2]=[]  #tuple不能修改
# ()to string
print(mytuple.__str__() + "xxx")
strx="\'ccc\' 'xxx' "
print(rf"{strx}")


def _date(value: date) -> str:
    return r"DATE '{year:d}-{month:02d}-{day:02d}'".format(
        year=value.year, month=value.month, day=value.day
    )


print(_date(date(2022, 2, 2)))

# =====================================================
print("=========================6===========================")
stu = {"aaa", "bbb", "aaa", "ccc"}
stu.add("xxx")
print(stu)

a = set("abcde")
b = set("bcdef")
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# {}to string
print("*".join(stu))

# =====================================================
print("==========================7==========================")

mydict = {"id": 1, "name": "小明"}
print(mydict)

print(str(mydict["id"]) + " " + mydict["name"])

mydict["name"] = "小华"
print(str(mydict["id"]) + " " + mydict["name"])

mydict2 = dict([("id", 1), ("name", "小明")])
print(mydict2)

mydict3 = dict(id=1, name="小明")
print(mydict3)

# {k:v}to string
# =====================================================
print("=========================8===========================")
import json

data1 = {'b': 789, 'c': 456, 'a': 123}
encode_json = json.dumps(data1)
print(type(encode_json), encode_json)

decode_json = json.loads(encode_json)
print(type(decode_json))
print(decode_json['a'])
print(decode_json)
