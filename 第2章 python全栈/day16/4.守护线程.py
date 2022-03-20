
# from  threading import Thread
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
# if __name__ == '__main__':
#     t=Thread(target=task,args=('线程1',))
#     t.daemon = True
#     # 造线程非常快，因为不用开辟空间了
#     t.start()
#     print('主')
#     # 主线程掌管了这个进程里面的资源
#     #     # 主线程不会死了，资源是来自主线程的
#     #     # 主线程是这个进程里面的老大
# #     # 等待所有的子线程死了才死
# #     # 车间里面的厂长，员工下班了他才下班

# 所以守护线程需要等到非守护的所有线程都死了才死

from threading import Thread
from multiprocessing import Process
import time

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    # 进程
    # t1 = Process(target=foo)
    # t2 = Process(target=bar)
    # t1.daemon = True
    # # 创建进程的开销非常大，看你机器的配置,配置好123看得到
    # t1.start()
    # t2.start()
    # print('主')
    # 线程
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.daemon = True
    # 造线程非常快，因为不用开辟空间了
    t1.start()
    t2.start()
    print('主')
    # 因为456线程没有死掉
    # 守护线程 》》主线程 》》非守护线程
    # 按时下班的员工》》老板 》》加班的员工





