import asyncio
import threading
import time


async def coro_func():
    print(f"thread name {threading.current_thread().name} is Running at coro_func()")
    # sleep(3, 42) 表示在3秒后返回42
    return await asyncio.sleep(3, 42)


def another_thread(_loop):
    print(f"thread name {threading.current_thread().name} is Started")
    # _loop is a loop which was created in another thread
    future = asyncio.run_coroutine_threadsafe(coro_func(), _loop)
    print(f"Get future res at thread name {threading.current_thread().name}: {future.result()}")

    # _loop.run_until_complete(coro_func())  # RuntimeError: This event loop is already running

    print(f"thread name {threading.current_thread().name} is Finished")


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    main_th_cor = asyncio.sleep(5)
    # main_th_cor  is used to make loop busy with something until another_thread will not send coroutine to it
    print("START MAIN")
    x = threading.Thread(target=another_thread, args=(loop,), name="Some_Thread", daemon=True)
    x.start()
    time.sleep(1)
    loop.run_until_complete(main_th_cor)
    print("FINISH MAIN")
