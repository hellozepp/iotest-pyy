import time
import threading


class MyScheduler:
    def run(self, func, args=(), sec=0, minute=0, hour=0, day=0, once=True):
        if once:
            func(*args)
        schedule_thread = threading.Thread(target=self.__schedule_func, args=(func, args, sec, minute, hour, day))
        schedule_thread.daemon = True
        schedule_thread.start()

    @staticmethod
    def __schedule_func(func, args=(), sec=0, minutes=0, hour=0, day=0):
        while True:
            # 缺点：sleep是一个阻塞函数，只能执行固定间隔时间的任务，无法完成定时任务（在sleep的这一段时间，啥都不能做）
            time.sleep(day * 86400 + hour * 3600 + minutes * 60 + sec)
            func(*args)


if __name__ == '__main__':
    def print_time():
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


    scheduler = MyScheduler()
    scheduler.run(print_time, sec=2, once=False)
    time.sleep(10)  # 等待10秒
    print("main thread end")
