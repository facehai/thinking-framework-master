#  进程之间内存空间互相隔离，怎样实现共享数据 *****
# 进程之间内存数据不共享,但是共享同一套文件系统,所以访问同一个文件,是没有问题的
# 而共享带来的是竞争，竞争带来的结果就是错乱，如何控制，就是加锁处理
'''
抢票
    查票
    购票
互斥锁：
    在程序中进行加锁处理
    必须要释放锁下一个锁才能获取，所以程序在合适的时候必须要有释放锁
    如果不释放会导致程序阻塞，所以很危险。
所以用文件来处理共享数据
    1.速度慢
    2.必须有互斥锁
'''
import json
import  time,random
from multiprocessing import Process,Lock
def search(name):
    with open('db.json','rt',encoding='utf-8')as f:
        dic = json.load(f)
    # 模拟查票时间
    time.sleep(1)
    print('%s 查看到余票为%s'%(name,dic['count']))
# 第二个get子进程不会是第一个get子进程修改后count的结果
# 加互斥锁，把这一部分并发变成串行，
# 但是牺牲了效率，保证了数据安全
def get(name):
    with open('db.json','rt',encoding='utf-8')as f:
        dic = json.load(f)
        # 先看下有没有票
    if dic['count']>0:
            # 有票模拟填信息，付款，提交数据给服务端
        dic['count']-=1
        # 其他的进程全部都进来了
        time.sleep(random.randint(1,3))
        # 重新写入
        with open('db.json', 'wt', encoding='utf-8')as f:
            json.dump(dic,f)
            print('%s 购票成功'%name)
    else:
        print('%s查看到没有票了'%name)

def task(name,mutex):
    # 查票
    # 并发
    search(name)
    # 购票
    # 获取锁
    # # 串行
    mutex.acquire()
    get(name)
    # 释放锁
    mutex.release()
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=task,args=('路人%s'%i,))
#         p.start()
#         # 数据安全，是指读的时候无所谓，写的（改的）时候必须安全
#         # 写的时候是串行，读的时候并发
#         #  join只能将进程的任务整体变成串行
#
#         p.join()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p = Process(target=task,args=('路人%s'%i,mutex))
        p.start()
        # 数据安全，是指读的时候无所谓，写的（改的）时候必须安全
        # 写的时候是串行，读的时候并发
        #  join只能将进程的任务整体变成串行

        # p.join()