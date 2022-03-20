# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time,os,random
# # 模拟下载
# # 谁闲下来了谁去解析
# def get(i):
#     print('%s 下载进程 %s'%(os.getpid(),i))
#     time.sleep(3)
#     # 调用解析
#     parse(i)
# # 模拟解析
# def parse(i):
#     print('%s 解析进程结果为%s'%(os.getpid(),i))
#     time.sleep(1)
#
# if __name__ == '__main__':
#     p = ProcessPoolExecutor(9)
#     start = time.time()
#     for i in range(9):
#         future = p.submit(get,i)
#     p.shutdown(wait=True)
#     print('主',time.time()-start)
#     print('主',os.getpid())
# 这样get和parse耦合在一起
# 怎样实现解耦合
#
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,os,random
# 模拟下载
# 谁闲下来了谁去解析
# def get(i):
#     print('%s 下载进程 %s'%(os.getpid(),i))
#     time.sleep(random.randint(1,3))
#     # 调用解析
#     # parse(i)
#     return i
# # 模拟解析
# def parse(i):
#     i = i.result()
#     print('%s 解析进程结果为%s'%(os.getpid(),i))
#     time.sleep(1)
#
# if __name__ == '__main__':
#     p = ProcessPoolExecutor(9)
#     start = time.time()
#     for i in range(9):
#         future = p.submit(get,i)
#         # 添加一个任务回收
#         # 异步的9个进程会闲下来，闲下来的时候去做parse这个函数里面的事情
#         future.add_done_callback(parse)
#         #  parse会在任务运行完毕后自动触发,然后接收一个参数future对象
#         #         # 主进程处理解析，解析时间短，没必要去等下载完，由主进程一个(人)搞定
#         #         # 其他子进程专心下载
#     p.shutdown(wait=True)
#     print('主',time.time()-start)
#     print('主',os.getpid())

# io密集型,线程来做
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,os,random
from threading import current_thread
# 模拟下载
# 谁闲下来了谁去解析
def get(i):
    print('%s 下载线程 %s'%(current_thread().name,i))
    time.sleep(random.randint(1,3))
    # 调用解析
    # parse(i)
    return i
# 模拟解析
def parse(i):
    i=i.result()
    print('%s 解析进程结果为%s'%(current_thread().name,i))
    time.sleep(1)

if __name__ == '__main__':
    p = ThreadPoolExecutor(9)
    start = time.time()
    for i in range(9):
        future = p.submit(get,i)
        # 添加一个任务回收
        #         # 异步的9个线程会闲下来，闲下来的时候去做parse这个函数里面的事情
        future.add_done_callback(parse)
        # 异步调用:提交完一个任务之后,不在原地等待,而是直接执行下一行代码,
        #         # 会导致任务是并发执行的,,结果futrue对象会在任务运行完毕后自动传给回调函数
        #         #  parse会在任务运行完毕后自动触发,然后接收一个参数future对象
        #         # 那一个线程先结束下载就去处理解析，解析时间短，没必要去等其他线程下载完
    p.shutdown(wait=True)
    print('主',time.time()-start)
    print('主',current_thread().name)










