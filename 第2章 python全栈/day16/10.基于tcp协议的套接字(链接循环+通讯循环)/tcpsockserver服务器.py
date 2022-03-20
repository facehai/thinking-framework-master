import socketserver

class MyTCPhanler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                print('收到客户端数据',data)
                self.request.send(data.upper())
            except ConnectionResetError:
                break


if __name__ == '__main__':
    # 通信循环
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyTCPhanler)
    # 链接循环
    server.serve_forever()
