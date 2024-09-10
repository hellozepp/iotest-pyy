import time
from datetime import datetime

# ======================无时区=====================================
print("======================无时区=====================================")
print(time.gmtime(0))

print(time.gmtime())

print(time.gmtime(time.time()))

print(time.time())

# ======================本地时区=====================================
print("======================本地时区=====================================")

print(time.localtime())

# ===========================================================
print("===========================================================")

print(time.strptime("2016-01-12 22:10:30", "%Y-%m-%d %H:%M:%S"))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print("===============================print输出time3的毫秒值============================")
time1 = datetime.now()
time.sleep(1)
time2 = datetime.now()
time3 = (time2 - time1).microseconds
print("Duration in milliseconds:", time3 / 1000)
