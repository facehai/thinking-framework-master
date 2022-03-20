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
phone.send('hello'.encode('utf-8'))
phone.send('world'.encode('utf-8'))
phone.send('dahai'.encode('utf-8'))

# 收



# 4关机
phone.close()