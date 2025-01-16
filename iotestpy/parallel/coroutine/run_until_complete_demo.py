# 两种都是使用协程的
# 第一种是在主线程上启动两个协程任务哦
# 第二种的最佳方法也是启动两个协程
#
# 但是，它们运行方式是不一样的，
# 第一种：协程同步【就是一个一个任务交替运行】
# 第二种：协程并发【就是两个协程任务一并启动】
# 例子：使用pyppeteer打开浏览器就可以明确看出效果啦，用并发启动确实快，但是有点问题就是每个页面标签同步执行
# coding=utf-8
import asyncio
import functools
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [*] %(processName)s  %(threadName)s  %(message)s"
)


# def done_callback (loop, futu):
#     loop.stop()


async def work01(x):
    logging.info(f'Waiting :{str(x)}')
    await asyncio.sleep(x)
    logging.info(f'Done :{str(x)}')


# async def work02 (
#         loop,  # 第二种运行方式
#         x
# ):
#     logging.info(f'Waiting :{str(x)}')
#     await asyncio.sleep(x)
#     logging.info(f'Done :{str(x)}')
#     loop.stop()  # 第二种运行方式


if __name__ == '__main__':
    start = time.time()

    loop = asyncio.get_event_loop()
    # 第一种运行方式(这种写法也是在网上搜到的最多的协程运行方式，但从 Python3.7 版本开始，官方引入了一个新的、更简单的运行方式asincio.run，同样是实现上面代码的功能)
    loop.run_until_complete(work01(1))
    loop.run_until_complete(work01(3))
    # 第二种运行方式( 第二个协程没结束，loop 就停止了——被先结束的那个协程给停掉的。)
    # asyncio.ensure_future(work02(loop, 1))
    # asyncio.ensure_future(work02(loop, 3))
    # 解决第二种运行方式的最佳方法
    # futus = asyncio.gather(work02(loop, 1), work02(loop, 3))
    # futus.add_done_callback(functools.partial(done_callback, loop))

    # loop.run_forever()
    loop.close()
    logging.info(f"<程序退出> 总用时：{time.time() - start}")
