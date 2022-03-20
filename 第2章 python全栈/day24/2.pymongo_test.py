# python与mongodb进行交互
# 选择虚拟机上面的解释器
# va 对应 home/pyvip
import pymongo
# 建立链接
client = pymongo.MongoClient('127.0.0.1',27017)
# 指定数据库
db = client['mydb22']

# 指定集合
collection = db['stu']

# 增
# 插入一条
# collection.insert_one({'name':'aaa','age':18,'sex':'男'})
# 插入多条
# collection.insert_many([
#                     {'name':'xiaobai','sex':'男','age':18},
#                     {'name':'xiaohei','sex':'女','age':16},
#                     {'name':'xiaohong','sex':'男','age':18}
#                     ])

# 改
# 修改一条
# collection.update_one({'name':'aaa'},{'$set':{'age':888}})
# 修改多条
# collection.update_many({'name':'aaa'},{'$set':{'age':888}})

# 删除
# 删除一条
# collection.delete_one({'name':'aaa'})
# 删除多条
# collection.delete_many({'name':'aaa'})
# 删除所有
collection.delete_many({})

# 查全部
data=collection.find()
# 游标
# print(data)
for i in data:
    print(i)

# 查一条
# data1=collection.find_one()
# print(data1)

# 逻辑和比较查询
# data2=collection.find(
# {'$or':
#                 [{'$and':[{'sex':'女'},{'age':16}]},
#                 {'$and':[{'sex':'男'},{'age':{'$gte':19}}]}]
#             }
# )
# # 游标
# # print(data)
# for i in data2:
#     print(i)