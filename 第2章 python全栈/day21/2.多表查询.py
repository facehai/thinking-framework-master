'''
create table dep(
id int,
name varchar(20)
);

create table emp1(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
);
insert into dep values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营');

insert into emp1(name,sex,age,dep_id) values
('大海','male',18,200),
('夏洛','male',48,201),
('西施','female',38,201),
('顾安','male',28,202),
('周瑜','male',18,200),
('诸葛','male',18,204)
;
1.笛卡儿积
查的时候是整体一起查
select * from emp1,dep;
select * from emp1,dep where emp1.dep_id = dep.id;
select * from emp1,dep where emp1.dep_id = dep.id and dep.name = '技术';
多表连表最好不要用where过滤
#2、内连接：只取两张表有对应关系的记录
select * from 表名 inner join 表名 on 条件
select * from emp1 inner join dep on emp1.dep_id = dep.id;
select * from emp1 inner join dep on emp1.dep_id = dep.id where dep.name = '技术';

#3、左连接: 在内连接的基础上保留左表没有对应关系的记录
select * from 表名 left join 表名 on 条件
select * from emp1 left join dep on emp1.dep_id = dep.id;

#4、右连接: 在内连接的基础上保留右表没有对应关系的记录
select * from 表名 right join 表名 on 条件
select * from emp1 right join dep on emp1.dep_id = dep.id;

#5、全连接：在内连接的基础上保留左、右面表没有对应关系的的记录
select * from emp1 left join dep on emp1.dep_id = dep.id
union
select * from emp1 right join dep on emp1.dep_id = dep.id;

如果是外键好的就有对应关系
join on
select name,age,bname,price from author join book join author2book on author.id =author2book.author_id and book.id = author2book.book_id;

'''