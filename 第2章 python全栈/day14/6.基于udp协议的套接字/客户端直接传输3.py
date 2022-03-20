import socket
import time
# udp用SOCK_DGRAM数据报
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
i = 0
while True:
    i += 1
    # 爱收就收，不收也会把操作系统数据清清除
    client.sendto(('helloc%s'%i).encode('utf-8'),('127.0.0.1',8080))
    # 发空也可以，因为报头有数据
    time.sleep(1)
    data,server_addr = client.recvfrom(1024)
    print(data)