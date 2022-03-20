'''
视图是什么?  *****
    本质是一张虚拟的表
    数据来自select语句，在内存里面，是一个临时数据
    那么有没有办法把它保存
    视图可以
    但是它可以永久保存表的结构，数据来源与原始的表，
    保存的是查询语句
    每次查询都是那种select语句去原始表里面查
如何使用
    创建视图
        语法
            create view 视图表的名字 as select语句
        实例
            create view test_view1 as select * from t1 where name = 'xialuo';
有什么用?
    原表安全
    案例:  在一公司中需要一张表保存所有人的薪资信息
           这个表不是所有人都能全看到   老板 财务 可以
           某一个员工 只能看到自己的信息
           所以不能把整个表的信息开发给这个员工
           工资保密协议
    功能1,隐藏部分数据 开放指定的数据
    insert into test_view1 values(7,'xiaohai');
    视图有插入
    但是查询
    select * from test_view1;
    还是 as 后面的 select * from t1 where name = 'xialuo';
    怎么证明
    insert into test_view1 values(3,'xialuo');
    同步到原表
    select * from t1;
    功能2,因为视图可以将查询结果保存特性 我可以用视图 来达到减少书写sql的次数
    技术部门都有那些员工
    select * from emp1 join dep on emp1.dep_id = dep.id where dep.name = '技术';
    将查询结果作为一个视图 以后在使用到这个需求 就直接查看视图
    注意:字段名不能重复
    create view jishu as select emp1.*,dep.name as dep_name from emp1 join dep on emp1.dep_id = dep.id where dep.name = '技术';
修改视图
    语法
        alter view 视图名称 as sql语句
    实例
        alter view test_view1 as select * from t1 where name = 'xiaohai';
删除视图
    语法
        drop view 视图名称
    实例
        drop view test_view1;
特点
     1.每次对视图进行的查询 其实都是再次执行了 as 后面的查询语句
     2.可以对视图进行修改 修改会同步到原表
     3.视图是永久存储的  存储的不是数据  而就是一条 as sql语句
     4.不要改视图，视图很多，只是用来查

'''