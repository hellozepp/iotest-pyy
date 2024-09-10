import subprocess
# 这两个模块都可以在当前主进程中创建子进程，但不同的是multiprocessing中的进程主要是运行python代码，而subprocess中的进程是运行已经编写好的程序，或者说是shell命令。
subprocess.run("echo aaa", shell=True)

# =======================================================================
print("=======================================================================")
# run 会阻塞当前进程，直到子进程执行完毕
p = subprocess.run("ls /", shell=True, stdout=subprocess.PIPE)
print(p.stdout.decode("utf-8"))

# =======================================================================
print("=======================================================================")
p = subprocess.run(["python3", "./testpy.py"], input=b"xxx\n", stdout=subprocess.PIPE)
print(p.stdout.decode("utf-8"))

# =======================================================================
print("=======================================================================")

data = b"test\n"
p = subprocess.Popen(["python3", "./testpy.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
res = p.communicate(input=data)
print(res[0].decode("utf-8"))
