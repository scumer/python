# -*- coding: utf-8 -*-
from mongoengine import *
from datetime import datetime

# 连接数据库
connect('XDB')   # 连接本地blog数据库
# 如需验证和指定主机名
# connect('blog', host='192.168.3.1', username='root', password='1234')

# 定义分类文档
class Categories(Document):
    ' 继承Document类,为普通文档 '
    name = StringField(max_length=30, required=True)
    artnum = IntField(default=0, required=True)
    date = DateTimeField(default=datetime.now(), required=True)
    




