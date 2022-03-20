'''
# 事务可以包含一系列的sql语句，事务的执行具有原子性 *****
#原子性：
#包含多条sql语句要么都执行成功，要么都执行不成功
create table tt1(id int,name varchar(12));
insert into tt1 values(1,'dahai');
开启事务
start transaction;
提交事务
commit;
回滚
rollback;

#transaction:事务，交易

'''