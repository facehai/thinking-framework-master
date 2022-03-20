'''
整型
    表示整数,通常id设置成整型 int
    存储范围(-2147483648,2147483647)
    强调：整型类型后面的宽度限制的根本不是存储宽度，限制的是显示宽度
    create table t5(id int(1));
    create table t6(id int(5));

    create table t7(id int zerofill);
    create table t8(id int(5) zerofill);
2. 浮点型:小数
    单精度和双精度
        数字的个数最大值为255,小数最大值为30
    单精度
        float(255,30)
    双精度
        double(255,30)
    准确精度(小数是最精确)
        decimal
        数字的个数最大值为65,小数最大值为30
    create table tt8(x float(255,30));
    create table tt9(x double(255,30));
    create table tt10(x decimal(65,30));

    insert into tt8 values(1.11111111111111111111111111111111111111);
    insert into tt9 values(1.11111111111111111111111111111111111111);
    insert into tt10 values(1.11111111111111111111111111111111111111);
3.日期类型
    year 1999
    date 1999-11-11
    time 08:30:00
    datetime/timestamp 1999-11-11 08:30:00

    create table student(
        id int,
        name varchar(16),
        a_year year,
        b_date date,
        class_time time,
        reg_time datetime
        );
    插入当前的时间
        insert into student values
        (1,'dahai',now(),now(),now(),now());
    自定义的数字时间
        insert into student values
        (1,'dahai',2000,20001111,083000,20001111083000);
    自定义的字符串数字时间
        insert into student values
        (1,'dahai','1999','2000-11-11','08:30:00','2000-11-11 08:30:00');
    datetime/timestamp
        在实际应用的很多场景中，MySQL的这两种日期类型都能够满足我们的需要，存储精度都为秒，
        但在某些情况下，会展现出他们各自的优劣。下面就来总结一下两种日期类型的区别。
    1.DATETIME的日期范围是1001——9999年，TIMESTAMP的时间范围是1970——2038年。

    2.DATETIME使用8字节的存储空间，TIMESTAMP的存储空间为4字节。因此，TIMESTAMP比DATETIME的空间利用率更高。

    3.DATETIME的默认值为null；TIMESTAMP的字段默认不为空（not null）,默认值为当前时间（CURRENT_TIMESTAMP）。
        create table time1(x timestamp);
        create table time2(x datetime);
4.字符类型
    注意: 宽度指限制字符的个数
    char：定长
        char(5)
    varchar 变长
        varchar(5)
    相同点: 宽度指的都是最打存储的字符个数,超过了都无法正常存储
    不同点
        char(5)
            'm'---》'm     ' 5个字符
        varchar(5)
            'm'----> 'm'   1个字符 （还有一个bytes是描述数据的）
char(5)
dahai|aa   |xxx  |f    |
varchar(5)
1个bytes+dahai|1个bytes+aa|1个bytes+xxx|1个bytes+f|
varchar(5)大部分用它 ,大部分情况下存储的数据都是小于约束的宽度
5.enum枚举是多选一，像python布尔类型,
    set集合是多选多 了解
    create table student1(id int,
    name varchar(20),
    sex enum('man','woman'),
    hobbies set('read','play','music'));
    插入数据
    insert into student1 values(1,'dahai','man','read,play');


'''