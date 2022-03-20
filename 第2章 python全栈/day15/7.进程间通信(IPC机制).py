'''
速度快  *****
锁问题解决
ipc机制
    进程彼此之间互相隔离，要实现进程间通信（IPC），
    multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的
    共享内存空间
    队列=管道+锁
'''
from multiprocessing import Queue
# 占用的内存，最好小数据，消息数据，下载地址
# Queue(限制队列里面的个数)
# 先进先出
q=Queue(3)
# 添加
q.put('a')
q.put('b')
q.put({'a':2})
print('篮子满了')
# 队列满了，相当于锁了
# q.put({'a':2})

# 提取
print(q.get())
print(q.get())
print(q.get())
# # 队列为空，等待加入，也会阻塞，相当于锁了
print('队列为空')
print(q.get())





