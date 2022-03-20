# 没有实现真正意义的并发
# 只是说收发消息很快
# 原因是由于数据量太小
# 客户端太少
import time
import socket
# udp用SOCK_DGRAM数据报
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))


while True:
    # 接收的是数据和客户端的ip和端口元组
    data,client_addr=server.recvfrom(1024)
    print(data)
    print(client_addr)
    time.sleep(3)
    server.sendto(data.upper(),client_addr)