# *****
import time,random
from  multiprocessing import Process,JoinableQueue
def producer(name,food,q):
    for i in range(10):
        res = '%s%s'%(food,i)
        # 模拟生产数据的时间
        time.sleep(random.randint(1,3))
        q.put(res)
        print('厨师%s生产了%s'%(name,res))
def consumer(name,q):
    while True:
        # 订单都没来还在等呢
        # 生产者往消费者发信号
        res = q.get()

        # 模拟处理数据的时间
        time.sleep(random.randint(1, 3))
        print('吃货%s吃了%s' % (name, res))
        # 1每次完成队列取一次，往q.join() ，取干净了q.join()运行完
        q.task_done()
if __name__ == '__main__':

    start = time.time()
    q = JoinableQueue()
    # 生产者
    p1 = Process(target=producer,args=('大海','包子',q))
    p2 = Process(target=producer,args=('中海','辣椒炒肉',q))
    p3 = Process(target=producer,args=('小海','土豆丝',q))
    # 消费者
    c1 = Process(target=consumer,args=('夏洛',q))
    c2 = Process(target=consumer,args=('西施',q))
    # #3.守护进程的作用: 主进程死了，消费者子进程也跟着死
    #     #把消费者变成守护进程
    c1.daemon = True
    c2.daemon = True
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
    # 2消费者task_done给q.join()发信号
    q.join()
    # 队列已经为空
    print('主',time.time()-start)
    # 生产者运行完？1,2
    # 消费者运行完？1,2
    # 意味着print('主')执行主进程运行完了，生产者消费者也运行完了
    # 但是消费者还是阻塞，可以用守护进程结束掉子进程