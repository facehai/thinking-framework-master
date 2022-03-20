# 每次更新本地文件记得上传，运行的是虚拟机上面的文件 *****
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
# 创建表
sql = '''
create table t1(
    id int not null,
    name varchar(10)
    );
'''
try:
    cursor.execute(sql)
    print('创建成功')
except Exception as e:
    print('创建数据库表失败%s'%e)
finally:
# 关闭游标连接# 相当与exit，关闭mysql
    cursor.close()
# 关闭数据库连接# 回收资源
    client.close()

