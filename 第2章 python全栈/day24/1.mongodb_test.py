'''
mongodb
可以分散存储到多台服务器上面，分布式存储
利用位置服务器去定位存储信息

数据处理：数据是存储在硬盘上的，只不过需要经常读取的数据会被加载到内存中，将数据存储在物理内存中，从而达到高速读写。

MongoDB是面向文档的数据库，不是关系型数据库。将数据库存储为一个文档，文档类似与json格式,没有表结构，想加就加
适合场景：事件的记录，内容管理或者博客平台等等。(经常变化的数据)
    记录日志
        可以放到mongodb
            {
            时间:2021.9.22
            地点:长沙
            状态:正常
            }
        游戏场景
        用户装备信息，属性信息
            {
            头部:xxx头盔
            上衣:xxx a
            裤子:xxx b
            }

进入mongodb
mongo
退出
exit
mongodb的库
    查看所有数据库
        库里面必须有数据才能查看到
        只是创建了库是隐式创建，只有库里面有数据才会真正意义的存在
        show dbs
    切换/创建数据库
        use mydb2
    查看所在库
        db
    删除库
        db.dropDatabase()
mongodb的集合操作
    创建集合
        db.createCollection('stu')
    查看当前数据库的集合
        show collections
    删除集合
        db.stu.drop()
mongodb的文档操作
    增：
        语法
            db.集合名称.insert(文档)
        实例
            不插入id自动生成id
                db.stu.insert({name:'xiaoming',age:18})
            自己插入id
                db.stu.insert({'_id':3,name:'xiaoming',age:18})
        插入多条
            语法
                db.集合名称.insert([
                        一条文档,
                        二条文档,
                        三条文档
                        ])
            实例
                db.stu.insert([
                    {name:'xiaobai','sex':'男',age:18},
                    {name:'xiaohei','sex':'女',age:16},
                    {name:'xiaohong','sex':'男',age:18}
                    ])
    查：
        整体查询
            语法
                一般
                    db.集合名称.find()
                美观查询
                    db.集合名称.find().pretty()
        指定查询
            语法
                db.stu.find({某个文档})
            实例
                db.stu.find({name:'xiaoming'})
        筛选
            语法
                db.stu.find({某个文档的key:values为1代表显示/values为0代表不显示})
            实例
                db.stu.find({name:'xiaoming'},{age:1})
                db.stu.find({name:'xiaoming'},{age:0})
        逻辑运算符
            and 与
            or 或
        比较运算符
            gt 大于
            lt 小于
            gte 大于或等于
            lte 小于或等于
            ne 不等于
        语法
                {$and:[包含多个条件]}
                {$or:[包含多个条件]}
        实例
            db.stu.find({$and:[{sex:'女'},{age:16}]})
            查询条件1或者条件2的数据
            条件1：性别女并且年龄16岁
            条件2：性别男并且年龄大于或等于18岁

            db.stu.find({$or:
                [{$and:[{sex:'女'},{age:16}]},
                {$and:[{sex:'男'},{age:{$gte:18}}]}]
            })
    改：
        只会修改一条数据 并且其他字段也没有了
            db.stu.update({name:'xiaohong'},{name:'xianghonghong'})
            age:18被去掉了
        只会修改一条数据 并且其他字段保留
            db.stu.update({name:'xiaobai'},{$set:{age:66}})
        修改多条数据 并且其他字段保留
            db.stu.update({name:'xiaobai'},{$set:{age:66}},{multi:true})
    删：
        只删除符合条件的第一条数据
            db.stu.remove({age:66},{justOne:true})
        删除符合条件的所有数据
            db.stu.remove({age:66})
        删除所有数据
            db.stu.remove({})









'''