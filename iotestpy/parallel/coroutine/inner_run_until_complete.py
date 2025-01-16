import asyncio
import websockets


# 错误示例 - 不要这样做
# async def wrong_way():
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(some_task())  # 错误：在异步函数中调用 run_until_complete
#     loop.run_forever()  # 错误：事件循环已经在运行


# 正确示例 1 - 简单的异步任务
async def simple_example():
    async def listen_messages():
        while True:
            await asyncio.sleep(1)
            print("Listening...")

    await listen_messages()  # 直接等待长期运行的任务


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(simple_example())


# 正确示例 2 - 多个异步任务
async def multi_task_example():
    async def task1():
        while True:
            await asyncio.sleep(1)
            print("Task 1 running")

    async def task2():
        while True:
            await asyncio.sleep(2)
            print("Task 2 running")

    # 创建任务
    await asyncio.gather(task1(), task2())


if __name__ == "__main__":
    asyncio.run(multi_task_example())


# 正确示例 3 - 在类中使用事件循环
class AsyncManager:
    def __init__(self):
        self.loop = None
        self._thread = None

    def start(self):
        async def run_tasks():
            while True:
                await asyncio.sleep(1)
                print("Running in background")

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(run_tasks())

    def stop(self):
        if self.loop:
            self.loop.stop()
            self.loop.close()