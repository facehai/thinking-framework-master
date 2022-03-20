'''
file--->setting,选择console Font，右侧primary font即设置console端的字体和大小
#1、完整语法(语法级别关键字的排列顺序如下)
select distinct 字段1,字段2,字段3,... from 库名.表名
                    where 约束条件
                    group by 分组依据
                    having 过滤条件
                    order by 排序的字段
                    limit 限制显示的条数
                    ;
# 关键字执行的优先级
from
where
group by
having
distinct 去除
order by
limit
'''
def fromm():
    '''
    找到表，返回表
    :return:
    '''
    pass
def where(f):
    '''
    过滤整张表
    :return:
    '''
    pass
def group(res1):
    '''
    第一次过滤后分组
    :return:
    '''
    pass
def having(res2):
    '''
    分组后再次筛选
    :return:
    '''
    pass
def distinct(res3):
    '''
    去重
    :return:
    '''
    pass
def order(res4):
    '''
    排序
    :return:
    '''
    pass
def limit(res5):
    '''
    限制结果的显示条数
    :return:
    '''
    pass
def select():
    f=fromm()
    res1=where(f)
    res2=group(res1)
    res3=having(res2)
    res4=distinct(res3)
    res5=order(res4)
    limit(res5)
'''
创建表
    create table emp(
    id int not null unique auto_increment,
    name varchar(20) not null,
    sex enum('male','female') not null default 'male', #大部分是男的
    age int(3) unsigned not null default 28,
    h_date date not null,
    post varchar(50),
    post_comment varchar(100),
    salary double(15,2),
    office int, #一个部门一个屋子办公室
    depart_id int # 部门id
    );

插入数据


insert into emp(name,sex,age,h_date,post,salary,office,depart_id) values
('西施','male',18,'20170301','tuling',7300.33,401,1), #以下是教学部
('大海','male',78,'20150302','teacher',1000000.31,401,1),
('夏洛','male',81,'20130305','teacher',8300,401,1),
('顾安','male',73,'20140701','teacher',3500,401,1),
('诸葛亮','male',28,'20121101','teacher',2100,401,1),
('周瑜','female',18,'20110211','teacher',9000,401,1),
('刘邦','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('美美','female',48,'20150311','sale',3000,402,2),#以下是销售部门
('九九','female',38,'20101101','sale',4000,402,2),
('攒攒','female',18,'20110312','sale',5000,402,2),
('西西','female',18,'20160513','sale',6000,402,2),
('东东','female',28,'20170127','sale',7000,402,2),

('段誉','male',28,'20160311','operation',3000,403,3), #以下是运营部门
('乔峰','male',18,'19970312','operation',4000,403,3),
('东邪','female',18,'20130311','operation',5000,403,3),
('西毒','male',18,'20150411','operation',6000,403,3),
('北丐','female',18,'20140512','operation',7000,403,3)
;
# 简单查询
select * from emp;
查询单个字段
select post from emp;
去除某个字段的重复
select distinct post from emp;
查看员工的月薪
select name,salary from emp;
查看员工的年薪
select name,salary*12 from emp;
字段取别名
select name,salary*12 as year_salary from emp;
字符串拼接 concat
select concat('名字:',name) as new_name,concat('年龄:',age) as new_age from emp;
合并一列 拼接：
select concat(name,':',age)as name_and_age from emp;
一次性 concat_ws
select concat_ws(':',name,age,sex)as info from emp;

where
id 大于 10 小于 15 的员工
select * from emp where id > 10 and id < 15;
id 大于或等于 10 小于或等于 15 的员工
select * from emp where id >= 10 and id <= 15;
等价
between
select * from emp where id between 10 and 15;

or
select * from emp where id = 6 or id = 9 or id =12;
等价
in
select * from emp where id in (6,9,12);

not
select * from emp where id not in (6,9,12);

like
_代表任意单个字符
%代表任意无穷个字符
select * from emp where name like '__';
select * from emp where name like '西%';

#3、group by分组
# 什么分组：按照所有记录相同的部分进行归类，一定区分度低的字段
# # 为何要分组：当我们要以组为单位进行统计时就必须分组，分组的目的是为了以组为单位进行统计的，再去考虑单条记录毫无意义
# 单条记录没有意义
select post from emp group by post;
这样不行
select name,age from emp group by post;
group_concat可以展示分组后字段的记录(一般不这样用)
select group_concat(name),group_concat(age) from emp group by post;

group by和聚会函数连用
max  最大
min  最小
avg 平均
sum  和
count  个数
按照部门分组
每个部门多少人
select post,count(id) from emp group by post;
每个部门最高薪资人
select post,max(salary) from emp group by post;
每个部门平均薪资
select post,avg(salary) from emp group by post;
每个部门总共薪资
select post,sum(salary) from emp group by post;
性别分组
男人多少个，女人多少个
select sex,count(id) from emp group by sex;

# 统计出每个部门年龄30以上的员工的平均薪资
第一步先把30岁以上的员工过滤出来
    select * from emp where age >= 30;
第二部分组部门，配合聚合函数
    select post,avg(salary) from emp where age >= 30 group by post;
# 注意：分组是在where之后发生的,聚合函数不能和where连用
    select * from emp where max(salary)> 3000;
where > group by > having
#4、having 过滤条件
# where是在分组之前的过滤，即在分组之前做了一次整体性的筛选 
# having是在分组之后的过滤，即在分组之后专门针对聚合的结果进行进一步的筛选    
每个部门的平均薪资
    select post,avg(salary) from emp group by post;
筛选平均薪资大于10000的部门的平均薪资
    select post,avg(salary) from emp group by post having avg(salary) > 10000;
筛选平均薪资大于10000且小于200000的部门的平均薪资
    select post,avg(salary) from emp group by post having avg(salary) > 10000 and avg(salary) < 200000;
查询各个部门包含的员工小于2的岗位名和员工
group_concat 可以展示字段名
select post,group_concat(name),count(id) from emp group by post having count(id) < 2;

去除某个字段的重复
    distinct
查询平均薪资5000的部门并只展示一条
    select avg(salary) from emp group by post having avg(salary);
    select distinct avg(salary) from emp group by post having avg(salary) = 5000;

#5、order by排序
年龄排序
小到大
    select * from emp order by age asc;
大到小
    select * from emp order by age desc;
# 先按照age升序排列，如果age相同则按照salary降序排
    select * from emp order by age asc,salary desc;
部门平均薪资排序 ，因为是分组之后的排序
    select post,avg(salary) from emp group by post order by avg(salary);
不看部门只看平均薪资（去重）
    select distinct avg(salary) from emp group by post order by avg(salary);

#6、limit 限制显示的条件
    select * from emp limit 3;
#薪资最高那个人的详细信息
   利用排序
   select * from emp order by salary desc limit 1;
   
#分页显示
   select * from emp limit 0,5;    
   select * from emp limit 5,5;    

'''