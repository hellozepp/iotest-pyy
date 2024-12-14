from multiprocessing import Pool
import time

import multiprocessing


def worker():
    print('Worker')


if __name__ == "__main__":
    '''
    Python有三种启动多进程的方法：

    fork启动方法：可以更快地进行写时复制，复制此进程的整个内存。由于速度更快，可以在需要派生出大量进程或快速派生进程的情况下使用。但是，由于fork不复制parent中的线程，因此在出现锁竞争的情况下，子进程可能会继承不必要的线程等其他不必要的开销。此外，由于子进程会继承父进程中的所有资源，包括文件描述符和网络接口，因此在特定情况下可能会带来一些问题。因此，使用fork的时候需要谨慎。
    spawn启动方法：父进程开始一个全新的 python 解释器进程。子进程将仅继承运行进程对象run()方法所需的资源。特别是，父进程中不必要的文件 Descriptors 和句柄将不会被继承。与使用* fork 或 forkserver *相比，使用此方法启动进程的速度相当慢。在任何Python版本中都可以使用，它启动了一个干净的新进程来运行Python代码。使用spawn方法的好处在于从父进程中不继承任何资源。目标Python进程从头开始启动，并具有与父进程孤立的空间。 这样可以避免死锁等问题，但是启动时间相对较长，因为处理器必须加载、初始化Python解释器本身，并从磁盘读取模块以及其他资源等。因此，如果需要启动一些子进程并且需要充分利用系统资源，可以使用spawn。
    forkserver启动方法：使用较新的Python版本，可以避免父进程中的锁同步问题和开销。 当从父进程中启动一个子进程时，将从创建的“fork server”进程中获取一个子进程，并在派生子进程之间重用。 因为“fork server”是干净的，没有绑定到特定工作负载，所以可以避免在从父进程派生后不同进程之间共享的问题。使用该方法的优点是可以在处理器上派生许多子进程，且运行时间也相对较快。
    
    set_start_method('spawn')被调用来设置使用spawn启动方法。接着，一个新的子进程被创建，并在子进程中执行worker函数。使用join等待子进程完成并退出。注意，必须在__name__ == '__main__'下运行不然可能会发生错误。
    '''
    multiprocessing.set_start_method('spawn')
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
