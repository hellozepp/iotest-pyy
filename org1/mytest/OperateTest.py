# coding= utf-8


# 规定 " / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
# Python算术运算符操作
print("Python算术运算符操作")
'''
+	加 - 两个对象相加	a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/	除 - x除以y	b / a 输出结果 2.0
%	取模 - 返回除法的余数	b % a 输出结果 0
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
'''
print(9 ** 2)
print(9 / 2)
print(9 % 2)
print(9 // 2)
print("5,", 9.6 / 3.2)
print("6,", 9.6 % 3.2)  # X
print("7,", 9.6 // 3.2)  # ? bug
print("8,", 10 // 5)
print("9,", 15.9 // 5.3)
print("10,", 4.5 // 5)  # 0.0

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)

print("=========比较运算符===========")
'''
运算符	描述	实例
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
<>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 true。

'''
print("=========逻辑与或非===========")
'''
运算符	逻辑表达式	描述	实例
and	    x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的值。 	(a and b) 返回 20。
or	    x or y	布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	    not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''
a = 0
b = 20
# python 中的and从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值。
#
# or也是从左到有计算表达式，返回第一个为真的值。
if (a and b):
    print("1 - 变量 a 和 b 都为 true", a and b)
else:
    print("1 - 变量 a 和 b 有一个不为 true", a and b)  # 0

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true", a or b)  # 20
else:
    print("2 - 变量 a 和 b 都不为 true", a or b)

# 修改变量 a 的值
a = 20
if (a and b):
    print("3 - 变量 a 和 b 都为 true", a and b)
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

a = 'first'
b = 'second'
print(1 and a or b)
print(0 and a or b)
a = ''
print(1 and a or b)  # a为假时，则出现问题
print((1 and [a] or [b])[0])  # 安全用法，因为[a]不可能为假，至少有一个元素 否则就不是三元运算的效果
magic_token = "xx"
DEFAULT_TOKEN_EXPIRE_TIME_MS = 123
token_expire_time_ms = 0 if magic_token is not None else DEFAULT_TOKEN_EXPIRE_TIME_MS
print(str(token_expire_time_ms))
print("=========位运算===========")
"""
运算符	描述	实例
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1 	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 	a >> 2 输出结果 15 ，二进制解释： 0000 1111
"""
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000 左移2位
print("5 - c 的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)
