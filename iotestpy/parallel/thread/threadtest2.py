import threading
import time


def doSomthing(name):
    for i in range(1, 3):
        print(name)
        time.sleep(1)


class do_start:
    def start(self):
        self.t1 = threading.Thread(target=doSomthing, args=("t1",))
        # t1.daemon=True

        self.t2 = threading.Thread(target=doSomthing, args=("t2",))
        self.t1.start()
        self.t1.join(10)  # 10秒后不再等待
        self.t2.start()
        self.t2.join()

        self.var1 = 1

        print(hasattr(self, 't2'))
        print(hasattr(self, 't1'))
        print(hasattr(self, 'var1'))

        print("main thread end")


do_start().start()
