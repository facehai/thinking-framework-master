'''
一对一
    学生表中的学生 对应的详细信息
    create table student(
        id int primary key,
        name varchar(10)
        );
    create table stu_detail(
        s_id int primary key,
        age int,
        sex char(5),
        foreign key(s_id) references student(id)
        on update cascade
        on delete cascade
        );
    插入数据
        insert into student values
        (1,'dahai'),
        (2,'xialuo'),
        (3,'xishi');
        insert into stu_detail values
        (1,18,'man'),
        (2,18,'man'),
        (3,18,'woman');
    select * from student,stu_detail;
    select * from student,stu_detail where student.id = stu_detail.s_id;

'''