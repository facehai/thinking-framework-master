import socket

# 1买手机
# AF_INET 互联网协议
# SOCK_STREAM TCP流式协议,
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(phone)

# 2.拨号
phone.connect(('127.0.0.1',8080))

# 3.发/收消息
# 必须传入二进制，
# 物理层
while True:
    msg = input('>>.').strip()
    if len(msg) == 0:continue
    phone.send(msg.encode('utf-8'))

    # 收
    data = phone.recv(1024)
    print('收到服务端的数据',data.decode('gbk'))


# 4关机
phone.close()