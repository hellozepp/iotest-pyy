import asyncio
import threading


async def some_task(i):
    await asyncio.sleep(1)
    print(i)


async def production_task():
    print("production_task start")
    for i in "123":
        # 将不同参数some_task这个协程循环注册到运行在线程中的循环，
        # thread_loop会获得一循环任务
        # run_coroutine_threadsafe函数在新线程中建立新event_loop，可以动态添加协程，而不会阻塞主线程
        asyncio.run_coroutine_threadsafe(some_task(i), thread_loop)
        print(f"production_task {i}...")
        # 注意：run_coroutine_threadsafe 这个方法只能用在运行在线程中的循环事件使用

        # 线程中不能直接运行协程，需要将协程注册到事件循环中
        # thread_loop.run_until_complete(some_task(i)) # RuntimeError: This event loop is already running
    print("production_task done")


def start_loop(thread_loop):
    #  运行事件循环， loop以参数的形式传递进来运行
    asyncio.set_event_loop(thread_loop)
    thread_loop.run_forever()


if __name__ == '__main__':
    # 获取一个事件循环
    thread_loop = asyncio.new_event_loop()
    # 将次事件循环运行在一个线程中，防止阻塞当前主线程，运行线程，同时协程事件循环也会运行
    threading.Thread(target=start_loop, args=(thread_loop,), daemon=True).start()

    # 将生产任务的协程注册到这个循环中
    advocate_loop = asyncio.get_event_loop()
    # 运行次循环
    advocate_loop.run_until_complete(production_task())
