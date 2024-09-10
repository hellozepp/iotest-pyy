# 第二个
from threading import Thread
import time


def do(x):
    x = x * 3
    time.sleep(x * 600)


def main():
    threads = []
    for x in range(1, 3):
        t = Thread(target=do, args=(x,))
        t.start()
    for x in threads:
        x.join()

if __name__ == '__main__':
    main()