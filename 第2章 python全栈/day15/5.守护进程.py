#守护进程: 本质就是一个"子进程",该"子进程"的生命周期<=被守护进程的生命周期  *****
# 主进程运行完了，子进程没有存在的意义
# 皇帝和太监不是同生，但是是同死
from multiprocessing import Process
import time

def task(name):
    print('%s活着'%name)
    time.sleep(3)
    print('%s正常死亡'%name)

if __name__ == '__main__':
    p1 = Process(target=task,args=('老太监',))
    p1.daemon = True

    p1.start()

    time.sleep(1)
    print('皇帝正在死亡')


