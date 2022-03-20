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
# cursor() 只会把每条记录放入小元组
# cursor = client.cursor()
# 把字段也显示
#  显示成一个列表里面key是字段名 value是数据
cursor = client.cursor(pymysql.cursors.DictCursor)
# 查询
sql = 'select * from user;'

rows = cursor.execute(sql)

# print(rows)
# fetchall一次性拿到所有
# print(cursor.fetchall())
# # 第二次没了返回[]
# print(cursor.fetchall())
# 一次拿一条
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# # # 没有呢返回None
# print(cursor.fetchone())
# 拿指定的条数
# print(cursor.fetchmany(2))
# print(cursor.fetchone())
# 读一行指针移动一行
# 可以移动指针
# # 绝对位置移动 scroll(行数,mode='absolute') absolute绝对位置
# cursor.scroll(0,mode='absolute')
# cursor.scroll(1,mode='absolute')
# print(cursor.fetchall())
print(cursor.fetchone())
# 相对位置移动
cursor.scroll(1,mode='relative')
print(cursor.fetchone())

cursor.close()
client.close()









