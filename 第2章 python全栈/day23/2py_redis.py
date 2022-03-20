# python与redis进行交互
import redis
# 数据库是没有名称的，默认有16个，通过0-15来标识
con = redis.StrictRedis(
    host='127.0.0.1',
    port='6379',
    db= 4,
    decode_responses=True
)
# print(con)
# 字符串
# 有则增，无则改

# con.set('country','中国')

# 增加多个
# con.mset({'name':'dahai','city':'长沙'})
#查
# a = con.get('country')
# print(a)
# 有则增，无则改
# con.set('name','xiaohai')
# # 查多个 mget(多个key值)
# b = con.mget('name','city')
# print(b)
# # 删除
#
# con.delete('country')
# a = con.get('country')
# print(a)

# 列表
# 增
# con.rpush('list1','中国', '日本', '韩国', '印度', '新加坡', '马拉西亚')
# 改
# con.lset('list1',1,999)
# 删 # 在尾部删除一个数据
# con.lpop('list1')
# 查
# a = con.lrange('list1',0,-1)
# print(a)

# hash # key field value
# 增
# con.hmset('user',{'name':'dahai','city':'changsha','age':18,'sex':'男'})
# 改
# con.hset('user','age',888)
# 删除
# con.hdel('user','age')
# 查所有
# a= con.hgetall('user')
# print(a)
# 返回布尔类型
# a1 = con.hexists('user','name')
# print(a1)

# 集合 set类型  无序的字符集合  无序性 唯一性

# 增
# con.sadd('zset12','劳斯莱斯', '宾利', '迈巴赫', '法拉利', '兰博基尼')
# con.sadd('zset14', '宾利', '迈巴赫', '法拉利', '兰博基尼','宝马')
#指定删除
# con.srem('zset12','迈巴赫')
# 交集
# b=con.sinter('zset12','zset14')
# print(b)
# 并集
# b=con.sunion('zset12','zset14')
# print(b)
# 差集
# b=con.sdiff('zset12','zset14')
# print(b)



# 查
# a = con.smembers('zset12')
# print(a)


# 有序集合
# 增
# con.zadd('zset13',1,'韩信',2,'小乔',3,'妲己',4,'蔡文姬')
# 删
# con.zrem('zset13','韩信')


# 查
# a = con.zrange('zset13',0,-1)
# print(a)

# 全局命令
# 重命名
# con.rename('zset13','zset33')
# # 获取所有的keys
# print(con.keys())
# 设置过期时间
# con.expire('zset33',30)
# 查看过期时间  -1代表永久  -2过期
print(con.ttl('zset33'))
# 未过期之前设置 续费
# con.persist('zset33')


















