# *****
from multiprocessing  import Process
import time

# def task(name):
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is done'%name)
def task(name,n):
    print('%s is running'%name)
    time.sleep(n)
    print('%s is done'%name)

if __name__ == '__main__':

    # p1 = Process(target=task,args=('大海1',))
    # p2 = Process(target=task,args=('大海2',))
    # p3 = Process(target=task,args=('大海3',))
    # # 串行
    # # task('子1')
    # # task('子2')
    # # 主进程只是向操作系统发送了一个开启子进程的信号
    # p1.start()
    # p2.start()
    # p3.start()
    # # time.sleep(4)
    # # join让主进程等待子进程运行完
    # p1.join()
    # p2.join()
    # p3.join()
    # print('主')
    # 开启多个进程
    start = time.time()
    p_l = []

    for i in range(1,5):
        p = Process(target=task, args=('大海%s'%i,i))
        p_l.append(p)
        p.start()
    # # 主进程等待子进程
    for p in p_l:
        p.join()
    print('主',(time.time()-start))




