'''
1. 什么是GIL(全局解释器锁)
    互斥锁就是把多个任务的共享数据的修改由并发变成串行
    代码运行先拿到cpu的权限，还需要把代码丢给解释器，再在进程里面的线程运行

    GIL本质就是一把互斥锁,相当于执行权限
    每个进程内都会存在一把GIL,同一进程内的多个线程
    必须抢到GIL之后才能使用解释器来执行自己的代码,
    即同一进程下的多个线程无法实现并行,
    用不了多核（多个cpu）优势
    但是可以实现并发
    因为多线程是遇到io操作就会释放GIL锁
2. 为何要有GIL
    垃圾回收机制不是线程安全的
    每个进程内都会存在一把GIL
        意味着有锁才能计算
        多进程适合处理计算密集型
    多线程适合处理io密集型 所以多线程多核优势没有意义
3. 如何用GIL
    有了GIL,应该如何处理并发
'''
from  threading import Thread
import time
def task(name):
    print('%s is runing'%name)
    time.sleep(2)
if __name__ == '__main__':
    t1 = Thread(target=task,args=('线程1',))
    t2 = Thread(target=task,args=('线程2',))
    t3 = Thread(target=task,args=('线程3',))
    # 造线程非常快，因为不用开辟空间了
    t1.start()
    t2.start()
    t3.start()