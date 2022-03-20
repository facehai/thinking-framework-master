# *****
from multiprocessing import Process

n = 100

def task():
    global n
    # 改的是子进程里面的全局变量
    # 主进程里面没有改
    n = 0

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print(n)