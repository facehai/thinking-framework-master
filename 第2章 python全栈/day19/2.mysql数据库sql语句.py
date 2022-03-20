'''
登录
    mysql -uroot -pqwe123
退出
    exit
mysql的库
    就是一个文件夹
    文件夹:库（create/drop/alter/show）
        增
            语法
                create database 数据库名字 charset 编码格式（不需要加引号）
            实例
                create database dahai1 charset utf8;
        删
            语法
                drop database 数据库名
            实例
                drop database dahai1;
        改 字符编码
            语法
                alter database 需要修改的数据库名字 charset 字符编码
            实例
                alter database dahai1 charset gbk;

        查
            查看所有的库
                show databases;
            查看库的详细信息
                语法
                    show create database 数据库名
                实例
                    show create database dahai1;
字段类型  和  python的数据类型是一个道理
字符串类型 char varchar    整数类型  int   浮点型 float
文件: 表
    1.切换到库（文件夹）
        语法
            use 库名;
        实例
            use dahai1;
    增
        必须要use切换到当前数据库
            语法
                create table 表名(字段名 字段类型(宽度),字段名 字段类型(宽度)....);
            实例
                create table t1(id int,name varchar(11));
        不用切换数据库
            语法
                create table 库名.表名(字段名 字段类型(宽度),字段名 字段类型(宽度)....);
            实例
                create table dahai1.t2(id int,name varchar(11));
    删（彻底删除）
        语法
            drop table 表名
        实例
            drop table t2;
    改(一般不会改)
        1.添加字段
            语法
                alter table 表名 add 字段 类型（宽度）
            实例
                alter table t1 add sex char(11);
        2.删除字段
            语法
                alter table 表名 drop 字段
            实例
                alter table t1 drop sex;
        3.改表字段的字段类型
            1.改字段的类型（不改字段名）
                语法
                    alter table 表名 modify 字段 新类型(宽度)
                实例
                    alter table t1 modify name char(12);
            2.直接改字段和类型
                语法
                    alter table 表名 change 老子段 新字段（宽度）
                实例
                    alter table t1 change sex se varchar(11);
        4.修改表名
            语法
                rename table 表名 to 新表名
            实例
                rename table t1 to ta;
    查
        1.查看表结构
            语法
                desc 表名
            实例
                desc ta;
        2.查看创建的表
            语法
                show create table 表名
            实例
                show create table ta;
        3.查看所有的表
            语法
                show tables;
        4.查看所在的库
            select database();
文件内的一行行内容:记录(insert/delete/update/select)
    增
        1.为想要的字段添加值,多余的会插入空
            语法
                insert into 表名(字段1,字段2) values
                (第一行数据,没有插入的字段会为空),
                (第二行数据,没有插入的字段会为空),
                (第三行数据,没有插入的字段会为空);
            实例
                insert into ta(id,name) values
                (1,'dahai'),
                (2,'xialuo'),
                (3,'guan');
        2.不写添加的字段（所有字段插入）
            语法
                insert into(可以不写) 表名 values
                (第一行数据,记录必须与表的字段数量还有类型要一致),
                (第二行数据,记录必须与表的字段数量还有类型要一致),
                (第三行数据,记录必须与表的字段数量还有类型要一致);
            实例
                insert ta values
                (4,'dahai','man');
    删
        删除表的部分信息
            语法
                delete from 表名 where 条件
                不要用它全删:没有条件全删
            实例

                delete from ta where id = 1;
        清空表信息
            语法
                truncate 表名
            实例
                truncate ta;
    改
        1.直接修改字段
            语法
                update 表名 set 字段名 = 修改值
            实例
                update ta set se = 'woman';
        2.加条件
            语法
                update 表名 set 字段名 = 修改值 where 条件
            实例
                update ta set se = 'man' where id = 3;

    查
        1.查看所有的记录
            语法
                select * from 表名;
            实例
                select * from ta;
        2.查看指定字段
            语法
                select 指定字段 from 表名;
            实例
                select id,name from ta;
        3.查看字段加条件 where
            查看所有的加条件
                语法
                    select * from 表名 where 条件
                实例
                    select * from ta where id > 2;
        4.不用进入库也可以查表内容
            语法
                select * from 库名.表名
            实例
                select * from dahai1.ta;

















'''