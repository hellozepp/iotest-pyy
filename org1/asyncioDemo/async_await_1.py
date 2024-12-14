import asyncio
import time


# 受限与python是一门解析语言，其运行效率整体来说并不高（同时受困于全局解释器锁GIL，无法像java的框架一样做到真正的多线程），异步框架的需求应声而出
async def say_delay(msg, delay):
    await asyncio.sleep(delay)
    print(msg)


async def taskFun1():
    start = time.strftime('%H:%M:%S')
    print(f"begin at {start}")
    # await 表示在这个地方等待子函数执行完成，再往下执行。（在并发操作中，把程序控制权教给主程序，让他分配其他协程执行。） await 只能在带有 async 关键字的函数中运行。
    await say_delay('你好1', 1)
    await say_delay('你好2', 2)
    print(f"end at {time.strftime('%X')}")


# 两个异步任务是串行执行的，即第一个任务执行完毕后，第二个任务才开始执行，所以总共耗时3秒
asyncio.run(taskFun1())


async def taskFun2():
    print(f"begin taskFun2...")
    # 任务是用来调度协程的，以便并发执行协程。当一个协程通过 asyncio.create_task() 被打包为一个 任务，该协程将自动加入程序调度日程准备立即运行。
    task1 = asyncio.create_task(say_delay('你好1', 1))
    task2 = asyncio.create_task(say_delay('你好2', 2))
    start = time.strftime('%X')
    print(f"begin at {start}")
    await task1
    await task2
    # 统计时间差
    print(f"end at {time.strftime('%X')}")
    # 使用getter同时执行两个任务
    # await asyncio.gather(say_delay('你好1', 1), say_delay('你好2', 2))


# 两个任务是并行执行的，所以总共耗时2秒
asyncio.run(taskFun2())

print("==================不等待await=======================")


async def whattime(i):
    await asyncio.sleep(1)
    print(f'calling:{i}, now is {time.strftime("%X")}')


async def taskFun3():
    task = asyncio.create_task(whattime(0))
    await task
    # range 1-4
    for i in range(1, 5):
        asyncio.create_task(whattime(i))
    # 如果把这一行去掉或是sleep的时间小于1秒（比whattime()里面的sleep时间少即可），就会看不到后面四行的输出
    await asyncio.sleep(1)


asyncio.run(taskFun3())

import types


def function():
    return 1


def generator():
    yield 1


async def async_function():
    await asyncio.sleep(1)
    return 1


async def async_generator():
    yield 1


print(type(function) is types.FunctionType)
print(type(generator()) is types.GeneratorType)
print(type(async_function()) is types.CoroutineType)
print(type(async_generator()) is types.AsyncGeneratorType)
