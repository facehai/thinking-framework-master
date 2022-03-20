import socket

# 1买手机
# AF_INET 互联网协议
# SOCK_STREAM TCP流式协议,
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(phone)

# 2.插手机卡
phone.bind(('127.0.0.1',8080))
# 3开机
phone.listen(5)

# 4等待电话请求
print('start')
# # 建立三次握手
conn,client_addr=phone.accept()
# # 建立三次握手后的套接字
print(conn)
# 客户端的ip和端口
print(client_addr)

#5 收/发消息
#1024接收的最大字节数bytes
data = conn.recv(5)
print('第一次',data)

data = conn.recv(5)
print('第二次',data)

data = conn.recv(5)
print('第三次',data)
# 6挂电话链接
conn.close()

# 7关机
phone.close()

# 粘包问题是tcp协议流式传输数据的方式导致的
# 如何解决粘包问题:接收端能够精确地收干净每个数据包没有任何残留
# 所以客户端必须告诉服务端发送多少数据，就要有个报头
# 分析
# 报头的信息应该包含长度信息
# 问题1：发送的时候只能是Bytes类型
        # 描述长度的是数字
        # 所以我们应该把整型数字转换成固定长度的Bytes类型






