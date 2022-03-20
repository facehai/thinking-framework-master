import socket
import subprocess
# 1买手机
# AF_INET 互联网协议
# SOCK_STREAM TCP流式协议,
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(phone)

# 2.插手机卡
phone.bind(('127.0.0.1',8080))
# 3开机
# 等待连接的客户端
phone.listen(5)

# 4等待电话请求
print('start')
# # 建立三次握手
while True:
    conn,client_addr=phone.accept()
    # # 建立三次握手后的套接字
    print(conn)
    # 客户端的ip和端口
    print(client_addr)

    #5 收/发消息
    #1024接收的最大字节数bytes
    while True:
        # 客户端已经关闭，非正常断开来链接，服务端在用没有意义的conn，recv
        # 数据从客户端网线》》服务端网卡》》服务端操作系统 》》
        # 客户端关闭直接抛出异常 用try捕获
        try:
            cmd = conn.recv(1024)

            # shell：如果该参数为 True，
            # 将通过操作系统的 shell 执行指定的命令。
            # PIPE开启了一座桥，在2个进程之间
            # 命令stdout正确输出的结果
            # 命令stderr错误输出的结果
            obj = subprocess.Popen(cmd.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            print(len(stdout + stderr))
            conn.send(stdout + stderr)
            # 先发给自己的操作系统,保存在自己的操作系统里面,堆积在这里
        except ConnectionResetError:
            break
    # 6挂电话链接
    conn.close()

# 7关机
phone.close()
# 客户端关闭了服务端会正常结束
# 服务端必须满足至少三点:
# 1. 绑定一个固定的ip和port
# 2. 一直对外提供服务,稳定运行
# 3. 能够支持并发,
# 因为是io密集型要开多线程







