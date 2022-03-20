# 安装模块  pip install gevent
# 1.必须要放到文件的开头
# 打标记
from gevent import monkey
# 所有的io行为进行打包
monkey.patch_all()
# 导入gevent管理的任务
from gevent import spawn,joinall
import time
def play(name):
    print('%s play 1'%name)
    time.sleep(5)
    print('%s play 2'%name)

def eat(name):
    print('%s eat 1'%name)
    time.sleep(3)
    print('%s eat 2'%name)

start = time.time()
# 异步提交任务,不管结果，直接运行下行代码
g1=spawn(play,'大海1')
g2=spawn(play,'大海2')
# g1.join()
# g2.join()
# 一行代码搞定
joinall([g1,g2])
# time.sleep(4)
# 线程死了没了
print('主',time.time()-start)


