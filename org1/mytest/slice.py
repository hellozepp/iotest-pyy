# 洗牌：
print("洗牌")
import random

items = [1, 2, 3, 4, 5, 6]
print(random.shuffle(items))
print(items)  # 坑，洗牌没返回值
list = [20, 16, 10, 5]
random.shuffle(list)
print("随机排序列表 : ", list)

print("==============range================")
# 列表常用操作
li = [1, 2, 3, 4, 5, 6]  # 创建列表
print(li.__len__())
print(len(li))
print("操作数为：", 1, 2, 3, 4, 5, 6)
# 切片 slice
print(li[1:5])  # 结束开区间
print("迭代列表操作：")
li[-2] = 2
for x in li:
    print(x, sep=' ', end=" ")  # 结束符为空格
print("(done)")
print(":-1===", li[:-1])  # 结束开区间
print(li[0:])
print("两个[::]：：", li[::2])  # 跳一个
print(li[2::])  # 开始跳两下，其他不跳
print(li[::-2])  # 倒着跳一个
print(li[-2::])  # 只保留最后两个
print(li)
print(len(li))
print(li[4:2:-1])
print(li[4::-1])
print("在列表末尾添加新的对象")
li.append(7)
print(li[0:])
# 一次性追加另一个序列中的多个值
li.extend(li)
print(li)

# 总结：[-1] [:-1] [::-1] [n::-1]
# [-1]：获取最后一个元素；
# [:-1]：除了最后一个元素，获取其他所有的元素；
# [::-1]：对第一个到最后一个元素进行倒序之后取出；
# [n::-1]：对第一个到第n个元素进行倒序后取出。
print("总结：[-1] [:-1] [::-1] [n::-1]")
print("[-1]:", li[-1])
print("[:-1]:", li[:-1]) # 等价于li[0:-1]
print("[::-1]:", li[::-1])
print("[n::-1]:", li[2::-1])
li = [1]
# 如果只有一个元素，li[0:-1]会返回空列表
print("li[0:-1]:", li[0:-1])
print(li[0] if len(li) == 1 else li[0:-1])

