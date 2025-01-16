import queue
import threading
import time
from dataclasses import dataclass
from typing import Any

@dataclass
class Task:
    priority: int
    name: str
    data: Any
    
    def __lt__(self, other):
        # 定义对象之间的比较方法，用于优先级队列的排序，优先级越低的任务越先执行（小顶堆）
        return self.priority < other.priority

def producer(pq: queue.PriorityQueue, max_tasks: int):
    """生产者：产生一系列任务并放入队列"""
    for i in range(max_tasks):
        # 优先级按照 i % 3 循环，这样可以展示优先级效果
        priority = i % 3
        task = Task(
            priority=priority,
            name=f"Task-{i}",
            data=f"Data for task {i}"
        )
        
        print(f"Producer: Attempting to add {task.name} with priority {task.priority}")
        try:
            # 使用阻塞方式put，设置3秒超时
            pq.put(task, block=True, timeout=3)
            print(f"Producer: Successfully added {task.name}")
        except queue.Full:
            print(f"Producer: Queue full, couldn't add {task.name}")
        
        # 短暂休息，使得效果更明显
        time.sleep(0.5)

def consumer(pq: queue.PriorityQueue, max_tasks: int):
    """消费者：从队列中获取并处理任务"""
    tasks_processed = 0
    
    while tasks_processed < max_tasks:
        try:
            # 使用默认的阻塞方式get
            task = pq.get()
            print(f"Consumer: Processing {task.name} (Priority: {task.priority})")
            
            # 模拟处理任务的时间
            time.sleep(1)
            
            # 标记任务完成
            pq.task_done()
            tasks_processed += 1
            
        except queue.Empty:
            print("Consumer: Queue is empty")
            break

def main():
    # 创建一个较小的优先级队列来演示阻塞效果
    max_queue_size = 3
    max_tasks = 8
    
    pq = queue.PriorityQueue(maxsize=max_queue_size)
    
    # 创建生产者和消费者线程
    producer_thread = threading.Thread(
        target=producer, 
        args=(pq, max_tasks)
    )
    consumer_thread = threading.Thread(
        target=consumer, 
        args=(pq, max_tasks)
    )
    
    print(f"Starting demo with queue size {max_queue_size} and {max_tasks} tasks")
    
    # 启动线程
    producer_thread.start()
    consumer_thread.start()
    
    # 等待所有线程完成
    producer_thread.join()
    consumer_thread.join()
    
    print("Demo completed")

if __name__ == "__main__":
    main()
