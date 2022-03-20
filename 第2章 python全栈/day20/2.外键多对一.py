'''
外键
foreign key 限制关联表某一个字段的值必是来自于被关联表的一个字段
# foreign key注意：
# 1、被关联的字段必须是一个key，通常是id字段
# 2、创建表时：必须先建立被关联的表，才能建立关联表
    create table dep(
        id int primary key auto_increment,
        dep_name varchar(20),
        dep_info varchar(20)
        );
    语法
        constraint 外键名字      也可以不写
        foreign key(当前表需要关联的id,直接自己设置的名字) references 被关联的表名(被关联表的id)
        create table emp(
        id int primary key auto_increment,
        name varchar(15),
        age int,
        dep_id int,
        constraint fk_emp_dep
        foreign key(dep_id) references dep(id)
        );
    不写创建外键名
        create table emp(
        id int primary key auto_increment,
        name varchar(15),
        age int,
        dep_id int,
        foreign key(dep_id) references dep(id)
        );
    删除必须先删除关联的表
        drop table emp;
        drop table dep;
    删除外键（一般不用删除，外键的建立是考虑好了的）
        语法
            alter table 表名 drop foreign key 外键名字;
        实例
            alter table emp drop foreign key emp_ibfk_1;
    # 1,2
    # 3、插入记录时：必须先往被关联的表插入记录，才能往关联表中插入记录
        insert into dep(dep_name,dep_info) values
        ('python','python_course'),
        ('music','music_course'),
        ('java','java_course');

        插入关联表
        insert into emp(name,age,dep_id) values
        ('dahai',18,1),
        ('xishi',19,2),
        ('zuge',23,3),
        ('xialuo',24,1),
        ('zhouyu',21,3);
    删除时：应该先删除关联表emp中的记录，再删除被关联表对应的记录
    要删除部门表里面的一个id需要先把它被关联的字段删除
    delete from emp where dep_id = 2;
    删除
    delete from dep where id =2;
    改被关联表(改不了)
    update dep set id = 200 where id = 3;
    创建关联表可以更新同步和删除同步
        删除
        delete from dep where id =2;
        改被关联表(改不了)
        update dep set id = 200 where id = 3;
更新和删除同步，员工表设置成更新删除同步 on update cascade on delete cascade
        create table emp(
        id int primary key auto_increment,
        name varchar(15),
        age int,
        dep_id int,
        foreign key(dep_id) references dep(id)
        on update cascade on delete cascade
        );
查询
    select * from emp,dep;
    select * from emp,dep where emp.dep_id = dep.id;
    select * from emp,dep where emp.dep_id = dep.id order by emp.id asc;
    select * from emp,dep where emp.dep_id = dep.id order by emp.id desc;


'''