import time
from datetime import datetime
import tzdata

# ======================无时区=====================================
print("======================无时区=====================================")
print(time.gmtime(0)) # 偏移0秒的时间，即1970-01-01 00:00:00

print(time.gmtime())

print(time.gmtime(time.time())) # struct_time

print(time.time()) # 单位为秒的时间戳float

today = datetime.now()

print(f"today:{today}")  # datetime.datetime

# 代码显示当前的-关于本地机器的-日期和时间，然而，从datetime.now（）获得的datetime对象是一个简单的对象：它不知道任何关于其起源时区的信息
print(today.tzinfo) # None

# ======================本地时区=====================================
print("======================本地时区 CST=====================================")

print(time.localtime()) # struct_time
print(time.localtime().tm_zone) # CST 中国标准时间

# ===========================================================
print("===========================================================")

print(time.strptime("2016-01-12 22:10:30", "%Y-%m-%d %H:%M:%S"))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print("===============================print输出两次time的时间差============================")
time1 = datetime.now()
time.sleep(1)
time2 = datetime.now()
time3 = (time2 - time1).microseconds
print("Duration in milliseconds:", time3 / 1000)