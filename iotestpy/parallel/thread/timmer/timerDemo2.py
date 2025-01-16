from datetime import datetime
from threading import Timer
import time

'''
2 秒后打印当前时间。
'''


def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    timer = Timer(2, task, ())
    timer.daemon = True
    timer.start()


# 定时任务
def task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    timedTask()
    print("main thread is done")
    time.sleep(10)
