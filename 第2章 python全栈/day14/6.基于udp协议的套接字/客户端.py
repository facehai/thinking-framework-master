import socket
# udp用SOCK_DGRAM数据报
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input('>>>').strip()
    # 爱收就收，不收也会把操作系统数据清清除
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    # 发空也可以，因为报头有数据
    data,server_addr = client.recvfrom(1024)
    print(data)