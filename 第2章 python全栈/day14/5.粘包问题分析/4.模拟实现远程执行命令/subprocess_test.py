'''
1. 什么是进程
    进程指的是一个程序的运行过程,或者说一个正在执行的程序
    所以说进程一种虚拟的概念,该虚拟概念起源操作系统
subprocess模块
    sub   子
    process  进程
        正在进行中的程序   每当打开一个程序就会开启一个进程
        每个进程包含运行程序所需的所有资源
        正常情况下 不可以跨进程访问数据  qq不能访问微信，微信不能访问qq
        但是有些情况写就需要访问别的进程数据    美团跳转到支付宝  这里跨进程了
        提供一个叫做管道的对象 专门用于跨进程通讯
    作用:用于执行系统命令
    总结  subprocess的好处是可以获取指令的执行结果

'''
import subprocess
cmd = input('输入命令')
        # shell：如果该参数为 True，
        # 将通过操作系统的 shell 执行指定的命令。
        # PIPE开启了一座桥，在2个进程之间
        # 命令stdout正确输出的结果
        # 命令stderr错误输出的结果
obj=subprocess.Popen(cmd,
                 shell=True,
                 stdout= subprocess.PIPE,
                 stderr= subprocess.PIPE,
                 )
stdout=obj.stdout.read().decode('gbk')
stderr=obj.stderr.read().decode('gbk')
print(stdout+stderr)

















