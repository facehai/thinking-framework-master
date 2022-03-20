from threading import Thread,active_count,current_thread
import time,os
n = 100
def task():
    global n
    print('%s is running'%os.getpid())
    print('子%s'%current_thread().name)
    n = 0
    time.sleep(3)

if __name__ == '__main__':
    t = Thread(target=task)
    # 开启子线程
    t.start()
    # 等待子线程运行完
    t.join()
    # 线程的个数
    print(active_count())
    # 线程所在的进程pid
    print('主%s'%os.getpid())
    # 线程的名字
    print('主%s'%current_thread().name)
    # 同一个进程的所有线程资源共享
    print(n)

