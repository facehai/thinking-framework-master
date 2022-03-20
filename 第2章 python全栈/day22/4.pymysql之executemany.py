# 每次更新本地文件记得上传，运行的是虚拟机上面的文件  *****
# pip install pymysql
import pymysql
# 拿到套接字对象
client = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'qwe123',
    database = 'mysql14',
    charset = 'utf8'
)
# 拿到游标  mysql>
cursor = client.cursor()
# 插入以下列表的数据
userinfo = [
    (3,'aaaaaaa'),
    (4,'bbbbbbb'),
    (5,'ccccccc')

]
# 第一种方法
# for user in userinfo:
#     # print(user)
#     # print(user[0])
#     # print(user[1])
#     sql = 'insert into t1 values (%s,"%s");'%(user[0],user[1])
#     res = cursor.execute(sql)
#     print(res)
# 第二种方法
# 使用executemany的第二个参数，放入占位符的内容,占位符不需要引号，它可以自动识别
sql = 'insert into t1 values (%s,%s);'
res = cursor.executemany(sql,userinfo)
print(res)
client.commit()

cursor.close()
client.close()





