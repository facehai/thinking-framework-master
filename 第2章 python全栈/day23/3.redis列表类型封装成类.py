# 将redis的列表操作放法封装成类
import redis

class RedisList:
    def __init__(self,db = 5,decode_responses=True):
        self.conn = redis.StrictRedis(
    host='127.0.0.1',
    port='6379',
    db= db,
    decode_responses=decode_responses
)
    # 创建或者增加列表数据的操作 rpush, lpush
    # rpush key *value 但用python 去操作 rpush(key,*value)
    def push(self,key,push_var='r',*value):
        # print(value)
        if push_var == 'r':
            self.conn.rpush(key,*value)
        elif push_var == 'l':
            self.conn.lpush(key, *value)

    # lpop,rpop, lrem指定删除 count 0 代表全部
    #    count 也代表数量
    def pop(self,key,count,value,pop_var='r'):
        if pop_var == 'r':
            # 从右边删除
            self.conn.rpop(key)
        elif pop_var == 'l':
            #  从左边删除
            self.conn.lpop(key)
        elif pop_var == 'm':
            # 指定删除全部元素
            self.conn.lrem(key,count,value)
        elif pop_var == 'c':
            list2 = self.conn.lrange(key,0,-1)
            for value in list2:
                # 一个个进行# 指定删除全部元素
                self.conn.lrem(key, count, value)


    # 修改所在索引的元素lset lset key index value
    def set(self,key,index,value):
        self.conn.lset(key,index,value)

    # 查看列表元素所在的索引，lrange
    def get(self,key,start_index,end_index):
        print(self.conn.lrange(key,start_index,end_index))


a = RedisList(db=5,decode_responses=True)
# print(a.conn)
# 从右边插入列表数据
a.push('list1','r','张三','李四','王五')
# 从左边插入列表数据
# a.push('list1','l','张三','李四','王五')
# 修改指定索引的元素
# a.set('list1',2,'aaa')
# 从右边删除
# a.pop('list1','','')
# 从左边删除
# a.pop('list1','','','l')
# 指定删除一个或多个元素
# a.pop('list1',1,'张三','m')
# a.pop('list1',2,'李四','m')
# 指定删除全部元素
# a.pop('list1',0,'张三','m')
# 删除全部，不管什么元素
a.pop('list1',0,'','c')

# 查看列表
a.get('list1',0,-1)





