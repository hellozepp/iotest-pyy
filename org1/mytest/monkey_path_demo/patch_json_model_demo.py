import json
import ujson

# 通过monkey patch的方式，将json模块替换为ujson模块,monkey patch是一种在运行时动态修改代码的术语。
# 仅仅须要在进程startup的地方monkey patch即可了,是影响整个进程空间的。
# 同一进程空间中一个module仅仅会被执行一次。
def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads


monkey_patch_json()
print('main.py', json.__name__)

import sub

sub.sub()
