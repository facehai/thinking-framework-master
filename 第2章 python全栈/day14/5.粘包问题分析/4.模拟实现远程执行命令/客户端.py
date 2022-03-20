import socket
import struct
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
    # 五.先收报头
    header = phone.recv(4)
    # 六.从报头里解出真实数据的长度
    total_size=struct.unpack('i',header)[0]
    # 七. 接收真正的数据
    # 一次性接收好不好
    cmd_res = b''
    resv_size = 0
    while resv_size < total_size:
        # 假设是1024以下就一次接受完了
        # 如果大于1024是不是要多次
        # 可以把recv想象成一个袋子
        # 一次只能转1024
        data = phone.recv(1024)
        resv_size += len(data)
        cmd_res += data


    # data = phone.recv(total_size)
    print('收到服务端的数据',cmd_res.decode('gbk'))


# 4关机
phone.close()