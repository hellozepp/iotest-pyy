import queue
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


class QueueComparisonDemo:
    """队列类型详细对比演示"""

    @staticmethod
    def traditional_queue_demo():
        """传统同步队列演示"""
        print("\n--- 传统同步Queue演示 ---")
        # 创建固定大小队列
        q = queue.Queue(maxsize=5)

        def producer(name):
            """生产者线程"""
            for i in range(10):
                try:
                    # 阻塞式写入，超时2秒
                    item = f"数据-{name}-{i}"
                    q.put(item, block=True, timeout=2)
                    print(f"{name} 生产: {item}")
                    time.sleep(0.1)
                except queue.Full:
                    print(f"{name} 队列已满，等待中...")

        def consumer(name):
            """消费者线程"""
            while True:
                try:
                    # 非阻塞读取
                    item = q.get(block=False)
                    print(f"{name} 消费: {item}")
                    time.sleep(0.2)
                except queue.Empty:
                    break

        # 使用线程池
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.submit(producer, "生产者1")
            executor.submit(producer, "生产者2")
            executor.submit(consumer, "消费者1")
            executor.submit(consumer, "消费者2")

    @staticmethod
    async def async_queue_demo():
        """异步队列演示"""
        print("\n--- AsyncIO Queue演示 ---")
        # 创建异步队列
        q = asyncio.Queue(maxsize=5)

        async def async_producer(name):
            """异步生产者"""
            for i in range(10):
                try:
                    # 异步等待队列
                    item = f"异步数据-{name}-{i}"
                    await q.put(item)
                    print(f"{name} 异步生产: {item}")
                    await asyncio.sleep(0.1)
                except asyncio.QueueFull:
                    print(f"{name} 异步队列已满，等待中...")

        async def async_consumer(name):
            """异步消费者"""
            while True:
                try:
                    # 异步获取数据
                    item = await q.get()
                    print(f"{name} 异步消费: {item}")
                    await asyncio.sleep(0.2)
                    q.task_done()  # 标记任务完成
                except asyncio.QueueEmpty:
                    break

        # 创建协程任务
        producers = [async_producer(f"异步生产者{i}") for i in range(2)]
        consumers = [async_consumer(f"异步消费者{i}") for i in range(2)]

        # 等待所有任务
        await asyncio.gather(*producers, *consumers)

    @staticmethod
    async def async_advanced_features():
        """异步队列高级特性"""
        print("\n--- AsyncIO Queue 高级特性 ---")
        q = asyncio.Queue()

        # 1. 超时控制
        async def timed_get():
            try:
                # 带超时的获取
                item = await asyncio.wait_for(q.get(), timeout=1.0)
                return item
            except asyncio.TimeoutError:
                print("获取超时")
                return None

        # 2. 条件队列操作
        async def conditional_put():
            # 条件放入
            if q.qsize() < 10:
                await q.put("条件数据")

        # 3. 取消和异常处理
        async def cancellable_task():
            try:
                # 可取消的队列操作
                item = await asyncio.wait_for(q.get(), timeout=2.0)
            except asyncio.CancelledError:
                print("任务已取消")

        # 展示高级特性
        await q.put("初始数据")
        item = await timed_get()
        await conditional_put()


def main():
    # 同步队列演示
    QueueComparisonDemo.traditional_queue_demo()

    # 异步队列演示
    asyncio.run(QueueComparisonDemo.async_queue_demo())

    # 异步队列高级特性
    asyncio.run(QueueComparisonDemo.async_advanced_features())


if __name__ == "__main__":
    main()

# 面试队列特性对比
"""
Queue (同步队列) vs AsyncIO Queue (异步队列)

1. 线程模型
- Queue: 基于线程，阻塞式操作
- AsyncIO Queue: 基于协程，非阻塞异步操作

2. 等待机制
- Queue: thread.lock 实现等待
- AsyncIO Queue: 事件循环和future实现等待

3. 性能特点
- Queue: 适合CPU密集型任务
- AsyncIO Queue: 适合IO密集型任务

4. 使用场景
- Queue: 多线程并发
- AsyncIO Queue: 高并发网络编程

5. 取消和超时
- Queue: 需要复杂的同步机制
- AsyncIO Queue: 原生支持取消和超时

6. 同步原语
- Queue: threading.Lock
- AsyncIO Queue: asyncio.Lock

7. 通知机制
- Queue: .task_done(), .join()
- AsyncIO Queue: .task_done(), .join()的协程版本
"""
