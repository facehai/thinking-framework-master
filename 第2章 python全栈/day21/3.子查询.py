'''
多表查询的思路是把表连起来查询
子查询：就是将一个查询语句的结果用括号括起来当作另外一个查询语句的条件去用
先搞定一张表，再用这张表的条件去查询别的表
技术部门都有那些员工
多表查询
1.直接把表连接起来
select * from emp1 join dep on emp1.dep_id = dep.id;
2.然后在加上dep.name = '技术'
select * from emp1 join dep on emp1.dep_id = dep.id where dep.name = '技术';
子查询
1.先找到技术在的部门id
select id from dep where name = '技术';
2.通过找到的部门id去找员工表
select * from emp1 where dep_id = (select id from dep where name = '技术');
select * from emp1 where dep_id = 200;
技术部门和人力资源都有那些员工
select id from dep where name = '技术' or name = '人力资源';
select * from emp1 where dep_id in (200,201);
select * from emp1 where dep_id in (select id from dep where name = '技术' or name = '人力资源');

查询完一张单表也可以进行连表操作
# 每个部门最新入职的员工
先查询时间最大的
select post,max(h_date) from emp group by post;
取别名只是在内存里面 配菜
(select post,max(h_date) as max_date from emp group by post) as t2;
自己和自己连表
emp和emp过滤后的t2表进行连表
select * from emp as t1
inner join
(select post,max(h_date) as max_date from emp group by post) as t2
on t1.post = t2.post where t1.h_date = t2.max_date;




'''