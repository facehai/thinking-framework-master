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
# 插入数据
# sql  = '''
# insert into t1 values (1,'dahai'),(2,'xialuo');
# '''
# 修改数据
# sql = '''
# update t1 set name = 'xialuo' where id = 1;
# '''
# 删除数据
sql = '''
delete from t1 where id = 1;
'''


try:
    res=cursor.execute(sql)
    # # 几行受到影响
    print(res)
    # 需要提交
    client.commit()
except Exception:
    # 回滚
    client.rollback()
cursor.close()
client.close()


