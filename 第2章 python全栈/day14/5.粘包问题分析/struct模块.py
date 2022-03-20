# 把整型数字转换成固定长度的Bytes类型 ***
import struct
# 把数字转换成4个Bytes
obj1 = struct.pack('i',1000000)

print(obj1,len(obj1))

res1 = struct.unpack('i',obj1)

print(res1)
print(res1[0])
print(type(res1[0]))