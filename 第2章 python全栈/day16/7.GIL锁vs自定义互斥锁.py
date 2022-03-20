# 互斥锁意义在于，GIL它只是在计算型代码前后加锁，互斥锁可以在io操作前后加锁，保证数据安全
from threading import Thread,Lock
import time
n = 100
mutex=Lock()
def task():
    # 1 第一个线程抢到了GIL锁
    # 4 第二个线程抢到了第一个线程的GIL锁
    global n
    # 2 第一个线程抢到了自定义锁
    # 5 第二个线程卡在了自定义锁这里
    # 7 第二个线程抢到了第一个线程的自定义锁
    mutex.acquire()
    temp = n
    # 3 到了io只释放来GIL锁，没有释放自定义锁
    time.sleep(0.1)

    n = temp -1
    # 6 第一个线程完全的运行完自定义锁里面的代码，释放自定义锁
    mutex.release()
if __name__ == '__main__':
    t_l = []
    start = time.time()
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
    print(n,time.time()-start)




