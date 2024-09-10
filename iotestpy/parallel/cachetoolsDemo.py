import time
from datetime import datetime

from cachetools import TTLCache


def expensive_fun(arg1, arg2):
    key = (arg1, arg2)

    # 如果缓存中已经有计算结果，直接返回
    result = cache.get(key)
    if result is not None:
        cache[key] = result  # extend expire-time
        return result, 'cached'

    # 执行计算并将结果保存到缓存中
    time.sleep(1)  # expensive calc
    result = arg1 + arg2
    cache[key] = result
    return result, 're-calc'


## cache test
cache = TTLCache(maxsize=5, ttl=10)
for i in range(10):
    print(datetime.now(), expensive_fun(i, 2))
    print(cache.items())

print(cache.items())

for i in range(5):
    time.sleep(3)
    print(datetime.now(), expensive_fun(1, 2))
    print(cache.items())

# 等待缓存项已经过期
time.sleep(11)

# 再次调用需要重新计算，因为缓存项已经被清除了
print(datetime.now(), expensive_fun(1, 2))
