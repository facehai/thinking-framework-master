# 每次更新本地文件记得上传，运行的是虚拟机上面的文件
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
'''
# 创建表
create table user
    (id int,
    name varchar(20),
    password varchar(20)
    );
插入数据
insert into user values
(1,'dahai',123),    
(2,'xialuo',456),    
(3,'xishi',789); 

sql注入
用一些特殊符号来改变sql语句的运行逻辑，不需要账号和密码直接可以登录
-- 注释
第一种
select id from user where name = "dahai" -- dsadsadasdasdaff" and password = "%s";
用户名输入 dahai" -- dsadsadasdasdaff
密码不输入回车
登录成功
第二种
账号和密码都不需要
select id from user where name = "xxx" or 1=1 -- dsafdsafafafasfasfa" and password = "%s";
用户输入 xxx" or 1=1 -- dsafdsafafafasfasfa
相当于
select id from user where name = "xxx" or 1=1
密码不输回车
登录成功

有些网站的账号密码不允许输入特殊符合，为了防止sql注入
前端（浏览器页面）可以筛选，
但是如果用爬虫是不是可以跳过前端，
所以后端也要检测
'''
inp_user = input('输入账号名').strip()
inp_pwd = input('输入密码').strip()

sql = 'select id from user where name = "%s" and password = "%s";'%(inp_user,inp_pwd)

res=cursor.execute(sql)

if res:
    print('登录成功')
else:
    print('用户或密码错误')
cursor.close()
client.close()





