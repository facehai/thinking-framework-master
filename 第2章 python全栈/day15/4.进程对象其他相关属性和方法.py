# ***
#1. 进程pid:每一个进程在操作系统内都有一个唯一的id号,称之为pid

# from multiprocessing import Process,current_process
# import time
#
# def task():
#     print('%s is running'%current_process().pid)
#     time.sleep(30)
#     print('%s is done'%current_process().pid)
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     print('主',current_process().pid)


# # os模块也可以
# from multiprocessing import Process
# import time,os
#
# def task():
#     print('%s is running爹是 %s'%(os.getpid(),os.getppid()))
#     time.sleep(30)
#     print('%s is done爹是 %s'%(os.getpid(),os.getppid()))
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     #     # 谁把主进程创造出来的
#     #     #   用pycharm就是pycharm创造的
#     print('主%s爹是 %s'%(os.getpid(),os.getppid()))


#2. 进程对象其他相关的属性或方法 （了解）
from multiprocessing import Process
import time,os

def task():
    print('%s is running爹是 %s'%(os.getpid(),os.getppid()))
    time.sleep(30)
    print('%s is done爹是 %s'%(os.getpid(),os.getppid()))
if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    #     # 谁把主进程创造出来的
    #     #   用pycharm就是pycharm创造的
    # 进程的名字
    print(p.name)
    # 杀死子进程
    p.terminate()
    # 需要时间
    time.sleep(0.1)
    #  判断子进程是否存活
    print(p.is_alive())
    print('主%s爹是 %s'%(os.getpid(),os.getppid()))