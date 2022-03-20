'''
一、创建表的完整语法
#语法：
create table 库名.表名(
    字段名1 类型[(宽度) 约束条件],
    字段名2 类型[(宽度) 约束条件],
    字段名3 类型[(宽度) 约束条件]
);
约束条件：是在数据类型之外对字段附加的额外的限制
#注意：
1、最后一个字段之后不能加逗号
2. 在同一张表中，字段名是不能相同
3. 宽度和约束条件可选,字段名和类型是必须的
常用约束
    not null 非空
    default 默认值
    auto_increment 必须要加一个键 自增长 可以不用进行插入了
    primary key 主键 非空且唯一
实例
    create table t1(
        id int primary key auto_increment,
        name varchar(16) not null,
        sex enum('male','female') not null default 'male'
        );

    插入只用插入name
    insert into t1(name) values('dahai'),('xialuo'),('xishi');
auto_increment(自己设置初始值)
    实例
        create table tb51(
        id int primary key auto_increment,
        name varchar(20) not null
        )auto_increment = 100;
    insert into tb51(name) values('dahai'),('xialuo'),('xishi');

        delete from tb51;
    约束重置
        truncate tb51;
唯一约束
unique key
    实例
        创建方式一
            create table t2(x int unique);
        创建方式二
            create table t3(
            x int,
            unique key(x)
            );
联合唯一（二者加起来是唯一）
    create table service(
        ip varchar(15),
        port int,
        unique key(ip,port)
        );
    insert into service values
    ('1.1.1.1',3306);
primary key(非空唯一)
站在约束角度看primary key=not null unique
以后但凡建表，必须注意：
# 主键id
1、必须有且只有一个主键
2、通常是id字段被设置为主键
create table t5(
    id int primary key auto_increment
    );
    insert into t5 values();
联合主键（二者加起来是非空且唯一）
    create table t6(
    x varchar(15),
    y int,
    primary key(x,y)
    );
    insert into t6 values
    ('1.1.1.1',3306);

'''