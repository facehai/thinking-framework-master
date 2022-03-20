from threading import Thread
import  time
def task(name):
    print('%s is runing'%name)
    time.sleep(2)
    print('%s is done'%name)
if __name__ == '__main__':
    t = Thread(target=task,args=('线程1',))
    # 造线程非常快，因为不用开辟空间了
    t.start()
    print('主')
