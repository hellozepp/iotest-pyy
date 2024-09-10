import datetime
import time
import timerDemo
from apscheduler.schedulers.background import BackgroundScheduler


def timedTask(counter: timerDemo.counter):
    counter.inc()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", cur count is " + str(counter.get()))


if __name__ == '__main__':
    counter = timerDemo.counter()
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 1 秒
    scheduler.add_job(timedTask, 'interval', seconds=10, args=(counter,), id='test_job1')
    # 启动调度任务
    scheduler.start()
    time.sleep(500)
    print("ok!!")
