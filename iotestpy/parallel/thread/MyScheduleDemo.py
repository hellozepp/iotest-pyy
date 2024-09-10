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
            time.sleep(day * 86400 + hour * 3600 + minutes * 60 + sec)
            func(*args)


if __name__ == '__main__':
    def print_time():
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


    scheduler = MyScheduler()
    scheduler.run(print_time, sec=2, once=False)
    time.sleep(10)  # 等待10秒
    print("main thread end")
