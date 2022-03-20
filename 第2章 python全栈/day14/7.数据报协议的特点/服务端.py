# tcp协议可能是多发对应一收    数据流 *****
# 优点，传输数据更加可靠
# 缺点，每次传数据必须建立链接，每次发数据必须确认
# 下载，转载用tcp
# udp是一发对应一收 ，不会有粘包问题，数据报
# 稳定传输的字节512字节
# 优点，传输数据更快
# 缺点，数据容易丢失， 传输数据不可靠
# 用于聊天udp

import socket
# udp用SOCK_DGRAM数据报
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))

# 没有任何粘包问题
print(server.recvfrom(1024))
print(server.recvfrom(1024))