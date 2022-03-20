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
while True:
    # 客户端已经关闭，非正常断开来链接，服务端在用没有意义的conn，recv
    # 数据从客户端网线》》服务端网卡》》服务端操作系统 》》
    # 客户端关闭直接抛出异常 用try捕获
    try:
        data = conn.recv(1024)
        print('收到客户端的数据',data)
        # 变大写发送回去
        conn.send(data.upper())
    except ConnectionResetError:
        break
# 6挂电话链接
conn.close()

# 7关机
phone.close()








