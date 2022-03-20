'''
计算机开进程或者线程受限于计算机本身的硬件，所以就有了进程池和线程池限制最大进程或者线程数
不会造新的进程或者线程，不会浪费内存空间
'''
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,os,random
def task(name):
    print('%s%s is running'%(name,os.getpid()))
    time.sleep(random.randint(1,3))
    return 123
if __name__ == '__main__':
    # print(os.cpu_count())
    p=ProcessPoolExecutor(4)
    # 只会开4个进程的id
    # p.submit(task,'进程的pid')
    # p.submit(task,'进程的pid')
    # p.submit(task,'进程的pid')
    # p.submit(task,'进程的pid')
    # # # 节约了再次开辟进程空间
    # p.submit(task,'进程的pid')
    # p.submit(task,'进程的pid')
    # for i in range(20):
    #     # p.submit(task,'进程的pid')
    #     # 返回值
    #     future=p.submit(task, '进程的pid')
    #
    #     # print(future)
    #     # 同步调用
    #     print(future.result())
    # print('主')
#     异步
    l = []
    for i in range(10):
        # p.submit(task,'进程的pid')
        # 返回值
        future=p.submit(task, '进程的pid')

        # print(future)
        l.append(future)
    # #关闭进程池的入口,并且在原地等待进程池内所有任务运行完毕
    p.shutdown(wait=True)
    for future in l:
        # 一次性全部拿到结果
        print(future.result())
    print('主')



'''
提交任务的两种方式:
同步调用:提交完一个任务之后,就在原地等待,等待任务完完整整地运行完毕拿到结果后,再执行下一行代码,会导致任务是串行执行的
提交任务的方法，串行是任务的运行状态
异步调用:提交完一个任务之后,不在原地等待,结果???,而是直接执行下一行代码,会导致任务是并发执行的

'''




