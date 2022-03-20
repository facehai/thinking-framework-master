'''
1. 什么是生产者消费者模型
    生产者:代指生产数据的任务
    消费者:代指处理数据的任务
    该模型的工作方式:
        生产者生产数据传递消费者处理
        实现方式:
            生产者---->队列<------消费者
        厨师----》外卖小哥和外卖平台<-----消费者
        厨师不影响生产效率               不用等厨师炒完这道菜
        可以不停的炒菜                    就可以点别的菜
        炒好的菜可以给    外卖小哥
2. 为何要用
    当程序中出现明细的两类任务,一类负责生产数据,一类负责处理数据
    就可以引入生产者消费者模型来实现生产者与消费者的解耦合,平衡生产能力与消费能力,从提升效率

3. 如何用

'''
import time,random
from  multiprocessing import Process,Queue
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
        # 第十个是一个空
        if res is None:
            break
        # 模拟处理数据的时间
        time.sleep(random.randint(1, 3))
        print('吃货%s吃了%s' % (name, res))
if __name__ == '__main__':
    q = Queue()
    # 生产者
    p1 = Process(target=producer,args=('大海','包子',q))
    p2 = Process(target=producer,args=('中海','辣椒炒肉',q))
    p3 = Process(target=producer,args=('小海','土豆丝',q))
    # 消费者
    c1 = Process(target=consumer,args=('夏洛',q))
    c2 = Process(target=consumer,args=('西施',q))
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