from datetime import datetime
from threading import Timer
import time

'''
每个 10 秒打印当前时间。
'''


class counter:
    def __init__(self):
        self.c = 0

    def inc(self):
        self.c += 1

    def get(self):
        return self.c


def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数 TimerTaskCall#task
    第三个参数: 调用函数的参数(tuple)
    '''
    c = counter()
    _thread = Timer(1, call, (c,))
    _thread.daemon = True
    _thread.start()


# 定时任务
def call(c: counter):
    c.inc()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", cur count is " + str(c.get()))


if __name__ == '__main__':
    timedTask()
    # timedTask()
    time.sleep(200)
    print("main thread end")
