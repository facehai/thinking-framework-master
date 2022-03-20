from threading import Thread,Lock
import time
n = 100
mutex=Lock()
def task():
    global n
    # 线程1加锁
    mutex.acquire()
    temp = n
    # 在这个时间消耗完之前，后面的99个线程都进来了
    # 并且拿到的是temp=100
    # 效率高了，不安全
    # IO操作切换线程
    time.sleep(0.1)

    n = temp -1
    # 线程1计算完成释放锁
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




