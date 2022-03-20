# 计算密集型:应该使用多进程
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res = 0
#     for i in range(10000000):
#         res+=i
# if __name__ == '__main__':
#     l = []
#     # 查看cpu个数
#     print(os.cpu_count())
#     start = time.time()
#     for i in  range(8):
#         # 多进程8个cpu同时在算，计算效率高，但是进程之间切换效率低
#         # p = Process(target=work)
#         # 多线程是1个cpu在计算
#          # 毕竟计算效率低，但是切换效率高
#         p = Thread(target=work)
#
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     print('主%s'%(time.time()-start))

# IO密集型: 应该开启多线程
from multiprocessing import Process
from threading import Thread
import os,time

def work():
    time.sleep(2)
if __name__ == '__main__':
    l= []
    start = time.time()
    for i in range(20):
        # 进程之间切换效率低
        # p = Process(target=work)
        # 毕竟计算效率低，但是切换效率高
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()
    print('主%s'%(time.time()-start))











