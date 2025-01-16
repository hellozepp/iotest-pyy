import datetime
import time

from apscheduler.triggers.interval import IntervalTrigger

import timerDemo
from apscheduler.schedulers.background import BackgroundScheduler


def timedTask(counter: timerDemo.counter):
    counter.inc()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", cur count is " + str(counter.get()))


if __name__ == '__main__':
    counter = timerDemo.counter()
    # 创建后台执行的 schedulers APScheduler是一个 Python 定时任务框架，提供了基于日期、固定时间间隔以及 crontab 类型的任务，并且可以持久化任务、并以 daemon 方式运行应用。
    scheduler = BackgroundScheduler()
    # 启动调度任务
    scheduler.start()

    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 1 秒，关闭前一直执行
    scheduler.add_job(timedTask, 'interval', seconds=1, args=(counter,), id='test_job1')

    time.sleep(5)

    scheduler.shutdown()
    print("schedule 1 ok!!")

    scheduler = BackgroundScheduler()
    scheduler.start()

    # 延后3秒执行
    scheduler.add_job(timedTask, trigger='date', next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=3),
                      args=(counter,), id='test_job2')
    # 不主动关闭
    time.sleep(5)
    print("schedule 2 ok!!")
