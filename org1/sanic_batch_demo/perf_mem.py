import psutil
import os

info = psutil.virtual_memory()
import resource

soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_AS)
soft_limit = soft_limit / (1024 ** 2)
hard_limit = hard_limit / (1024 ** 2)
print("软限制（Soft Limit）：", soft_limit, "MB")
print("硬限制（Hard Limit）：", hard_limit, "MB")
import psutil

print("当前进程占用内存：", psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024, "MB")

mem = psutil.virtual_memory()
# 系统总计内存
zj = float(mem.total) / 1024 / 1024
# 系统已经使用内存
ysy = float(mem.used) / 1024 / 1024
# 系统空闲内存
kx = float(mem.free) / 1024 / 1024

print('系统总计内存:%d.3MB' % zj)
print('系统已经使用内存:%d.3MB' % ysy)
print('系统空闲内存:%d.3MB' % kx)
