from concurrent.futures import Future
import threading


def task_with_exception(future):
    try:
        # Simulate an operation that raises an exception
        raise ValueError("An error occurred in the task")
    except Exception as e:
        future.set_exception(e)


# Create a Future object
future = Future()

# Create and start a thread to run the task_with_exception function
thread = threading.Thread(target=task_with_exception, args=(future,))
thread.start()
thread.join()

# Handle the exception
try:
    result = future.result()
except Exception as e:
    print(f"Caught exception: {e}")

exception = future.exception()
if exception:
    print(f"捕获到异常: {exception}")
else:
    print("任务成功完成")
