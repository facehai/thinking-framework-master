import socketserver
import time

class MyUphander(socketserver.BaseRequestHandler):
    def handle(self):
        # 数据和套接字
        # print(self.request)
        data,sock=self.request
        print(data)
        time.sleep(1)
        sock.sendto(data.upper(),self.client_address)



if __name__ == '__main__':
    # 1.创建一个线程的通信循环
    server = socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyUphander)
    # 链接循环 serve_forever永远提供服务
    server.serve_forever()