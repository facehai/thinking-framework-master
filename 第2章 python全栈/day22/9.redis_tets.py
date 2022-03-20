'''
概述
    Redis本质上是一个Key-Value类型的内存数据库，整个数据库统统加载在内存当中进行操作，
    定期通过异步操作把数据库数据flush到硬盘上进行保存。因为是纯内存操作，Redis的性能非常出色，
    每秒可以处理超过 10万次读写操作。
    Redis的出色之处不仅仅是性能，Redis最大的魅力是支持保存多种数据结构，此外单个value的最大限制是1GB，
    redis不仅仅支持简单的Key-Value类型，同时还把value分为list,set,zset,hash等数据类型
    Redis的主要缺点是数据库容量受到物理内存的限制，不能用作海量数据的高性能读写，
    因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上。
    效率会远远高于mysql，但是存储的量级不如mysql
Redis有哪些适合的场景？
（1）、会话缓存（Session Cache）
最常用的一种使用Redis的情景是会话缓存（session cache）。用Redis缓存会话比其他存储（如Memcached）的优势在于：
Redis提供持久化。user: password

'''

# Redis的语句 *****
'''
redis是key-value的数据结构,每条数据都是一个键值对
键的类型是字符串
注意:键不能重复
值的类型分为五种
string ------》字符串
list  ------》列表
hash ------》哈希
set ------》集合
zset ------》有序集合
'''
'''
连接redis: 
redis-cli --raw
127.0.0.1:6379> ip 和 端口
退出 exit
默认使用的是0号数据库
数据库是没有名称的，默认有16个，通过0-15来标识
切换到其他数据库：
select n
# 1、string类型  一个key值对应一个value值
                name:dahai  age:18
增（改）
    语法
        set key value 设置一个key 值为value
        如果这个key存在，则更新value值
        如果这个key不存在，则就key value值存下来
    实例
        如果这个key不存在，则就key value值存下来
            set name dahai
        如果这个key存在，则更新value值
            set name xialuo
    追加数据：（在原来的字符上面增加）
        语法
            append key 字符
        实例
            append name 333
    一次设置多个key value(没有就增加)
        语法
            mset key value key value...
        实例
            mset name dahai sex girl age 18
删
    语法
        del key
    实例
        del name
查:
    语法
        get key
    实例
        get name
    一次获取多个value
        语法
            mget key1，key2，key3....
        实例
            mget name age sex
    获取所有的key
        keys *
其他的操作
    set num 333
incr会识别字符串里面的数字并加1
    incr num
decr会识别字符串里面的数字并减1
    decr num
incrby在原有的基础上增加100   
    incrby num 100 
decrby在原有的基础上减少100
    decrby num 100
过期时间(一秒为单位的)
比如会员 ，网盘链接    
    查看时间
        ttl key
        -1代表无限 -2代表不存在 
    expire age 30    
    要在时间还没有过期的时候
        撤销过期时间(续费会员)
        persist key
'''



























