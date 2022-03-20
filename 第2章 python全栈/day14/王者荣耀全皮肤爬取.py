# 王者荣耀url的地址
# https://pvp.qq.com
# 王者荣耀标准皮肤地址
# https://pvp.qq.com/web201605/herolist.shtml
# 需要点击图片产生新地址

# 云缨图片地址
# 标准皮肤地址
# # 推测图片有很多，
# 那么图片的编号是不应该是前端直接写好的，
# 而是后端通过数据库查询出来渲染到前端的，后端传入到前端应该用序列化json
# https://game.gtimg.cn/images/yxzj/img201606/heroimg/538/538.jpg
# 这个是点击进去的全部皮肤地址
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/538/538-bigskin-1.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/538/538-bigskin-2.jpg
# 艾琳图片地址
# 标准皮肤地址
# //game.gtimg.cn/images/yxzj/img201606/heroimg/155/155.jpg
# 这个是点击进去的全部皮肤地址
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/155/155-bigskin-1.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/155/155-bigskin-2.jpg
# 这个里面有数据
# https://pvp.qq.com/web201605/js/herolist.json
# 字典里面有 "ename": 538,

import requests
import os
from pyquery import PyQuery
# 1
# 分析目标网页
# 明确爬取的url路径

url='https://pvp.qq.com/web201605/js/herolist.json'
# 说明你是用浏览器访问的
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '87.0.4280.88 Safari/537.36'
}

# 2
# 发送requests请求
# 模拟浏览器发送请求
# 获取响应数据

herolist=requests.get(url,headers=headers).json()
# print(herolist)

# 3
# ​解析数据--json模块
# 把自己想要的数据解析出来
# #那我们遍历上面这个列表就能拿到每个英雄的字典数据

for i in herolist:
    # print(i['ename'],i['cname'],i['hero_type'])
    url_detail = 'https://pvp.qq.com/web201605/herodetail/%s.shtml'%i['ename']
    html = requests.get(url_detail).content

    doc = PyQuery(html)
    # print(doc)

    items = doc('.pic-pf').items()
    # print(items)
    # print(list(items))

    for item in items:
        print(type(item))
        # print(type(item))
        # 获取皮肤的名字
        name_datas = item.find('ul').attr('data-imgname')
        # print(name_datas.split('|'))
        name_data_list=name_datas.split('|')
    a = 0
    for name_data in name_data_list:
        a = a+1
        print(name_data)
#     #
        img='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%s/%s-bigskin-%s.jpg'%(i['ename'],i['ename'],a)
        print(img)
#     #
        hero_img_data=requests.get(img).content

        # 4
        # ​保存数据
        # 保存在目标文件夹中
        # 'img/英雄名字/皮肤图片'
        if os.path.exists('./王者') is False:
            os.mkdir('./王者')

        if not os.path.exists('./王者/%s'%i['cname']):
            os.mkdir('./王者/%s'%i['cname'])
        # 有的话直接保存
        with open('./王者/%s/%s.jpg'%(i['cname'],name_data),'wb') as f:
            f.write(hero_img_data)




