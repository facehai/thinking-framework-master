'''
多对多
    author2book 多对一     author
    author2book 多对一     book
    author      多对多     book
    create table author(
        id int primary key auto_increment,
        name varchar(16),
        age int
        );
    create table book(
        id int primary key auto_increment,
        bname varchar(16),
        price int
        );
    # 非主键可以混用
    create table author2book(
        id int primary key auto_increment,
        author_id int,
        book_id int,
        unique key(author_id,book_id),
        foreign key(author_id) references author(id)
        on update cascade on delete cascade,
        foreign key(book_id) references book(id)
        on update cascade on delete cascade
        );
    插入数据
        insert into author(name,age) values
        ('dahai',22),
        ('xialuo',23),
        ('guan',18),
        ('xishi',19),
        ('jiujiu',20);

        insert into book(bname,price) values
        ('玉女真经',5),
        ('九阳神功',3),
        ('太极拳',4),
        ('如来神掌',2),
        ('玉女剑法',6);

        insert into author2book(author_id,book_id) values
        (1,2),
        (1,3),
        (2,3),
        (2,4),
        (3,2),
        (3,3),
        (3,4),
        (4,3),
        (5,2);
查
    select * from author,book,author2book;
    select * from author,book,author2book;
    select author.id,name,age,bname,price from author,book,author2book where author.id =author2book.author_id and book.id = author2book.book_id;

    select author.id,name,age,bname,price from author,book,author2book where author.id =author2book.author_id and book.id = author2book.book_id and author.name ='dahai';

'''