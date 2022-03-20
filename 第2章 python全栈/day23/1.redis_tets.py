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

# 2、list类型 字符串列表

'''
key         value （字符串）
list1    1 2 3 4 5

增： 
    在插入数据时，如果该键不存在，redis将为新建一个该键
    右边添加
        语法
            rpush key value...   在尾部添加数据
        实例
            rpush list1 1 2 3 4 5
    左边添加
        语法
            lpush key value...   在头部添加数据    
        实例
            lpush list1 7 8 9    
            
查：
    指定索引下标查询
        语法
            lrange key start stop
        实例 
            lrange list1 0 3  
    查全部 -1表示最后一个数据
        lrange list1 0 -1
    根据index查看某个数据
        语法
            lindex key index
        实例
            lindex list1 1
改：
    修改某个下标的值
        语法
            lset key index value
        实例
            lset list1 1 99
删：
    右边删除 在尾部删除一个数据
        语法
            rpop key   
        实例
            rpop list1
    左边删除 在头部删除一个数据
        语法
            lpop key     
        实例
            lpop list1
    删除指定的数据：
        语法
            lrem key count value
        实例
            lrem list1 1 3
        删除list1中所有3 count 是 0代表所有
            lrem list1 0 3
    删除所有数据：
        语法
            del key
        实例
            del list1
            



'''
# 3、hash类型  是一个键值对集合 key key value
# key field(域) value
# field部分代表属性，value代表属性对应的值
# 特别适合存对象 user   name  value age value
'''
key                 value
user     username dahai sex girl age 18
增：
    语法
        hset key field value
    实例
        hset user name dahai
    存储多个
        hset user age 18    
    添加多个：
    语法
        hmset key field value...
    实例
        hmset user name xiaohai age 18 addr changsha 
查：
    查看指定的field 
    语法
        hget key field
    实例
        hget user name       
        hget user age       
    查看所有的field:  
    语法
        hkeys key
    实例
        hkeys user
    查看所有的value:  
    语法
        hvals key
    实例
        hvals user
    查看域值：（所有的field value）
    语法
        hgetall key
    实例
        hgetall user
    获取多个：
    语法
        hmget key field...
    实例
        hmget user name age
删
    删除指定
    语法
        hdel key field
    实例
        hdel user name
查看有几对field和value
语法
    hlen key 
实例
    hlen user
查看类型 
语法
    type key   
实例
    type user
'''
# 4、set类型  无序的字符集合  无序性 唯一性
'''
key     value
set1    1 2 3 4 5
增：
    语法
        sadd 集合 value....
    实例
        sadd set1 1 2 3 4 5
查：
    语法
        smembers key
    实例
        smembers set1
删：
    随机删除
        语法
            spop key count    
        实例
            随机删除一个元素
                spop set1
            随机删除3个元素
                spop set1 3
    指定删除：
        语法
            srem key members...
        实例
            srem set1 2 3   

其他：
    sadd set2 1 2 3 
    sadd set3 4 5 
    把3从set2中移动到set3
        smove set2 set3 3
    判断3是否在set3中  0代表不在  1代表在
    sismember set3 3
sadd set4 1 2 3 4
sadd set5 2 3 4 5

交集：
    sinter set4 set5
并集:
    sunion set4 set5 
差集
    sdiff set4 set5 

    
'''
# 5、Sorted Set类型 有序集合类型

'''
key           value
        权值  value
zset1    1 one 2 two ....
增：
    语法
        zadd 有序集合 权值 value...
    实例
        zadd zset1 1 one 2 two 3 three 1 four 1 five
查：
    通过索引查看(权值顺序)
        zrange zset1 0 -1
        倒序
        zrevrange zset1 0 -1
    通过权值查看2到3之间的元素（包括2和3）
        zrangebyscore zset1 2 3
    查看four的权值
        zscore zset1 four
    权值和value一起查看
        zrange zset1 0 -1 withscores
删
    直接删除five    
        zrem zset1 five    
    删除索引在0-1
        zremrangebyrank zset1 0 1
    删除权值再2-3
        zremrangebyscore zset1 2 3
'''

# 全局操作

'''
查看所有的key值
keys *
删除
del key
不存在 返回0  存在返回1
exists key   
重命名
rename key new_key


'''



































