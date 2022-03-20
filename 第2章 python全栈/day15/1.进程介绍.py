'''
1. 什么是进程 *****
    进程指的是一个程序的运行过程,或者说一个正在执行的程序
    所以说进程一种虚拟的概念,该虚拟概念起源操作系统
大前提:一个cpu同一时刻只能执行一个任务
    串行: 一个进程一个任务完完整整运行完毕才能执行下一个任务
            做完一件事情接着才能做下一件事
    并行: 多个任务是真正意义上的同时运行,只有多核才能实行并行
            相当于多个人在做多份工作
    并发: 多个任务看起来是同时运行的,单核下就能实现并发(并发=切换+保存状态)
        一个人做多件事，比如晚上回家，
        煮饭的时间可以切菜，炒菜，把衣服放到洗衣机，一次就做了多件事
         # 送外卖也是并发，有些外卖小哥一次接多个单
'''