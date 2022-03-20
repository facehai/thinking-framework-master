from  threading import Thread,current_thread
from socket import *

def client():
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.1',8080))
    n = 0
    while True:
        msg = '%s say hello %s'%(current_thread().name,n)
        n += 1
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))

if __name__ == '__main__':
    for i in range(500):

        t = Thread(target=client)
        t.start()