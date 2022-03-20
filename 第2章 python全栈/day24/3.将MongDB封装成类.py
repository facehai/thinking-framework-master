'''
将MongoDB find,insert,update,remove 方法封装成类
提示：就是把增删改查各封装成一个方法，一共8个封装成4个
find_one,find
insert_one ,insert_many
update_one, update_many
delete_one,delete_many
'''
import pymongo
# # 建立链接
# client = pymongo.MongoClient('127.0.0.1',27017)
# # 指定数据库
# db = client['mydb22']
#
# # 指定集合
# collection = db['stu']

class MyMongDB:
    def __init__(self,database,collection):
        # 把服务器建立连接赋值给实例化后的对象属性self.client
        self.client=pymongo.MongoClient('127.0.0.1', 27017)
        # 创建数据库给实例化后的对象属性self.db
        self.db=self.client[database]
        # 创建集合给实例化后的对象属性self.collection
        self.collection=self.db[collection]
    # insert_one ,insert_many
    def insert(self,*data):
        # 是一个元组
        # print(data)
        if len(data)==1:
            # 取元组的第一个值
            # 插入的是字典
            self.collection.insert_one(data[0])
        else:
            # 1 2
            # 元组要转换成列表
            # 插入的是一个列表里面包含的字典
            self.collection.insert_many(list(data))
    # update_one, update_many
    def update(self,data,new_data,m = False):
        if m:
            self.collection.update_many(data, {'$set': new_data})
        else:
            self.collection.update_one(data,{'$set':new_data})
    # delete_one,delete_many
    def remove(self,data,m=False):
        if m:
            self.collection.delete_many(data)
        else:
            self.collection.delete_one(data)


    # find_one,find
    def find(self,data={},m = False):
        if m:
            result = self.collection.find(data)
            # 游标
            for i in result:
                print(i)
        else:
            result = self.collection.find_one()
            print(result)


a=MyMongDB('mydb222','stu')
# 插入一个数据
# a.insert({'name':'dahai1'})
# 插入多个数据
# a.insert({'name':'dahai2'},{'name':'dahai3'})
# 修改一条数据
# a.update({'name':'dahai2'},{'name':'dahai222'})
# 修改多条数据
# a.update({'name':'dahai3'},{'name':'dahai333'},True)
# 删除指定的一条数据
# a.remove({'name':'dahai333'})
# 删除指定的多条数据
a.remove({'name':'dahai2'},True)

# 查找一个数据
# a.find({'name':'dahai1'})
# 查找全部个数据
a.find({},True)







