from multiprocessing  import Process
import time

def task(name):
    print('%s is running'%name)
    time.sleep(3)
    print('%s is done'%name)

# 开启子进程的操作必须放到
# if __name__ == '__main__'的子代码中
# 子进程不会再次加载
if __name__ == '__main__':
    # args
    # p = Process(target=task,args=('大海',))
    # kwargs
    p = Process(target=task,kwargs={'name':'大海'})

    # print(p)
    # 主进程只是向操作系统发送了一个开启子进程的信号
    p.start()
    # 1.操作系统先申请内存空间
    # 2.把主进程的数据拷贝到子进程里面
    # 3.调用cup才能运行里面的代码
    # 创造进程的开销大
    print('主')