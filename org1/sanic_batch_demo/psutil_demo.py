import sys
import time
import psutil

def get_cpu_info():
    # get pid from args
    if len(sys.argv) < 2:
        print("missing pid arg")
        sys.exit()

    # get process
    pid = int(sys.argv[1])
    p = psutil.Process(pid)

    # monitor process and write data to file
    interval = 60  # polling seconds
    with open("process_monitor_" + p.name() + '_' + str(pid) + ".csv", "a+") as f:
        print("time,cpu%,mem%,mem_mb\n")  # titles
        while True:
            current_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
            cpu_percent = p.cpu_percent()
            mem_percent = p.memory_percent()
            line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent) + ',' + str(p.memory_info().rss / 1024 / 1024)
            print(line)
            f.write(line + "\n")
            time.sleep(interval)


if __name__ == '__main__':
    # pid 71930
    sys.argv = ['psutil_demo.py', '71930']
    get_cpu_info()
