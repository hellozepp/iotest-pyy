from datetime import datetime
import sched
import time

'''
每个 10 秒打印当前时间。
scheduler 中的每个调度任务只会工作一次，不会无限循环被调用。如果想重复执行同一任务， 需要重复添加调度任务即可。
'''
def timedTask():
    # 初始化 sched 模块的 scheduler 类
    scheduler = sched.scheduler(time.time, time.sleep)
    # 增加调度任务 注意 sched 模块不是循环的，一次调度被执行后就 Over 了，如果想再执行，请再次 enter
    scheduler.enter(1, 1, task)
    # 运行任务
    scheduler.run()


# 定时任务
def task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    timedTask()
    time.sleep(10)
