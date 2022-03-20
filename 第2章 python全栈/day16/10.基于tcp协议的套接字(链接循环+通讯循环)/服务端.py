# 客户端关闭了服务端会正常结束
# 服务端必须满足至少三点:
# 1. 绑定一个固定的ip和port
# 2. 一直对外提供服务,稳定运行
# 3. 能够支持并发,
# 因为是io密集型要开多线程

import socket
from  threading import Thread
def communicate(conn):
    # 通讯循环
    while True:
        try:
            data = conn.recv(1024)
            print('收到客户端数据',data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
def server(ip,port,backlog=5):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(backlog)
    while True:
        # 链接循环
        conn,client_addr=server.accept()
        t = Thread(target=communicate,args=(conn,))
        t.start()
if __name__ == '__main__':
    s = Thread(target=server,args=('127.0.0.1',8080))
    s.start()