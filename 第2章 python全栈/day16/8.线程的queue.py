# 虽然线程中数据共享，但是队列可以处理锁的问题
# import queue
# q = queue.Queue(3)
#
# q.put(1)
# q.put(2)
# q.put(3)
# print('aaa')
# # q.put(4)
# print(q.get())
# print(q.get())
# print(q.get())
# print('bbb')
# print(q.get())
from threading import Thread,active_count
import time,random
# from  multiprocessing import Process,Queue
import queue
def producer(name,food,q):
    for i in range(10):
        res = '%s%s'%(food,i)
        # 模拟生产数据的时间
        time.sleep(3)
        q.put(res)
        print('厨师%s生产了%s'%(name,res))
def consumer(name,q):
    while True:
        # 订单都没来还在等呢
        # 生产者往消费者发信号
        res = q.get()
        # 第十个是一个空
        if res is None:
            #  主线程和最后一个线程
            if active_count() is 2:
                print(time.time()-start)

            break
        # 模拟处理数据的时间
        time.sleep(3)
        print('吃货%s吃了%s' % (name, res))
if __name__ == '__main__':
    start = time.time()
    q = queue.Queue()
    # 生产者
    p1 = Thread(target=producer,args=('大海','包子',q))
    p2 = Thread(target=producer,args=('中海','辣椒炒肉',q))
    p3 = Thread(target=producer,args=('小海','土豆丝',q))
    # 消费者
    c1 = Thread(target=consumer,args=('夏洛',q))
    c2 = Thread(target=consumer,args=('西施',q))
    # 生产者和消费者并发
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    # 生产完了
    p1.join()
    p2.join()
    p3.join()
    # 发结束信号给消费者
    # 发送给队列一个None
    q.put(None)
    q.put(None)
    print('主')


