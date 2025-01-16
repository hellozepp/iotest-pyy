import multiprocessing
import queue
import time
import random

def producer(q, name):
    """生产者进程函数"""
    for i in range(5):
        # 模拟生产数据
        item = f"{name}-data-{i}"
        time.sleep(random.uniform(0.1, 0.5))  # 随机延迟
        q.put(item)
        print(f"[生产者 {name}] 生产: {item}")

def consumer(q, name):
    """消费者进程函数"""
    while True:
        try:
            # 使用带超时的get方法
            item = q.get(block=True)
            print(f"[消费者 {name}] 消费: {item}")
            time.sleep(random.uniform(0.1, 0.3))  # 模拟处理时间
        except queue.Empty:
            print(f"[消费者 {name}] 队列为空，退出")
            break

def main():
    # 创建一个多进程队列
    queue = multiprocessing.Queue(maxsize=10)

    # 创建生产者进程
    producers = [
        multiprocessing.Process(target=producer, args=(queue, f"生产者-{i}"))
        for i in range(2)
    ]

    # 创建消费者进程
    consumers = [
        multiprocessing.Process(target=consumer, args=(queue, f"消费者-{i}"))
        for i in range(2)
    ]
    for p in consumers:
        p.start()

    time.sleep(3)
    # 启动所有进程
    for p in producers:
        p.start()


    # 等待生产者进程结束
    for p in producers:
        p.join()

    # 等待消费者进程结束
    for p in consumers:
        p.join()

    print("所有进程执行完毕")

if __name__ == "__main__":
    # 在Windows下需要添加这个保护
    multiprocessing.freeze_support()
    main()