import queue
import threading
import time
import random

def producer(q, name):
    """生产者函数，演示不同的put方法"""
    print(f"{name} 开始生产...")
    
    # 阻塞模式 - 默认行为
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
            # 非阻塞模式读取
            item = q.get(block=False)
            print(f"{name} 消费：{item}")
            q.task_done()  # 标记任务完成
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
        threading.Thread(target=producer, args=(q, f"生产者-{i}")) 
        for i in range(2)
    ]
    consumers = [
        threading.Thread(target=consumer, args=(q, f"消费者-{i}")) 
        for i in range(2)
    ]
    
    # 启动所有线程
    for t in producers + consumers:
        t.start()
    
    # 等待所有生产者完成
    for t in producers:
        t.join()
    
    # 等待队列处理完所有任务
    q.join()
    
    # 等待消费者完成
    for t in consumers:
        t.join()
    
    # 演示队列方法
    demonstrate_queue_methods()

if __name__ == "__main__":
    main()
