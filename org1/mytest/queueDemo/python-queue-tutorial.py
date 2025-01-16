import queue
import threading
import time
import random

"""
Python中的Queue模块提供了 3种队列：

Queue.Queue(maxsize):先进先出，maxsize为队列大小，其值为非正数的时候为 无限循环队列。

Queue.LifoQueue(maxsize):后进先出，相当于栈。

Queue.PriorityQueue(maxsize):优先级队列。
Python的queue.Queue实现细节：

线程安全性

完全线程安全
使用了threading.Lock()和threading.Condition实现并发控制
内部使用collections.deque作为存储容器


内部实现机制

不是直接使用数组或链表，而是使用了Python的collections.deque
deque是一个双端队列，支持高效的两端插入和删除
底层实现是一个动态数组（类似于链表+数组的混合结构）


与Java的ArrayBlockingQueue的主要区别
CopyPython Queue               Java ArrayBlockingQueue
-------------------------------------------------------------------------
动态大小                    固定大小
使用deque                  使用数组
条件变量同步                 ReentrantLock
更灵活的阻塞策略             相对更严格的阻塞

插入方式

默认是尾插法（FIFO - First In First Out）
提供了LifoQueue支持头插法（后进先出）
"""
def producer(q, name):
    """生产者函数，演示不同的put方法"""
    print(f"{name} 开始生产...")

    # 默认行为：阻塞模式
    try:
        for i in range(5):
            item = f"DATA-{name}-{i}"
            q.put(item, block=True, timeout=1)  # 阻塞模式，超时1秒
            print(f"{name} 生产：{item}")
            time.sleep(0.5)
    except queue.Full:
        print(f"{name} 队列已满，无法继续生产")


def consumer(q, name):
    """消费者函数，演示不同的get方法"""
    print(f"{name} 开始消费...")

    while True:
        try:
            # 非阻塞模式读取，读取不到数据时立即抛出异常
            item = q.get(block=False)
            #item = q.get(True, 3) # Waits for 3 seconds, otherwise throws `Queue.Empty`
            print(f"{name} 消费：{item}")
            # 在处理完一个项目后，可以使用 task_done() 方法通知队列管理器这个项目已经被处理完了。
            q.task_done()  # 标记任务完成，如果不调用，join会一直阻塞
        except queue.Empty:
            print(f"{name} 队列为空")
            break


def demonstrate_queue_methods():
    """演示Queue的各种方法"""
    print("\n--- Queue方法演示 ---")

    # 创建不同类型的队列
    fifo_queue = queue.Queue(maxsize=5)  # FIFO队列，最大长度5
    lifo_queue = queue.LifoQueue(maxsize=5)  # LIFO队列

    # 演示队列基本方法
    print(f"FIFO队列是否为空: {fifo_queue.empty()}")
    print(f"FIFO队列是否已满: {fifo_queue.full()}")

    # 添加元素
    for i in range(3):
        fifo_queue.put(i)
        lifo_queue.put(i)

    print(f"FIFO队列大小: {fifo_queue.qsize()}")
    print(f"LIFO队列大小: {lifo_queue.qsize()}")

    # 获取并移除元素
    print("FIFO取出:", fifo_queue.get())  # 先进先出
    print("LIFO取出:", lifo_queue.get())  # 后进先出


def main():
    print("Python Queue模块综合演示")

    # 创建一个有界队列
    q = queue.Queue(maxsize=10)

    # 创建生产者和消费者线程
    producers = [
        threading.Thread(target=producer, args=(q, f"生产者-{i}"), daemon=True)
        for i in range(2)
    ]
    consumers = [
        threading.Thread(target=consumer, args=(q, f"消费者-{i}"), daemon=True)
        for i in range(2)
    ]

    # 启动所有线程
    for t in producers + consumers:
        t.start()

    # 等待所有生产者完成
    for t in producers:
        t.join()

    # 阻塞等待队列处理完所有任务，注意因为我们消费会退出，所以这里不需要会卡死
    #q.join()  # if unfinished_tasks != 0: wait()

    # 等待消费者完成
    for t in consumers:
        t.join()

    # 演示队列方法
    # demonstrate_queue_methods()


if __name__ == "__main__":
    main()
