#!/usr/bin/python
#coding:utf-8

import requests
import random
url = 'http://m.jjl.cn/article/16040.html'
# 记录每次打开网页的标志，这里随机改变一下，有可能会重复
openudid = ('u15101956%s' % random.randint(10000, 99999))
param = {
    'vid':'0892123840010520',
    'appid':'6',
    'options':'{"0351502000020895":["0222991909030835"]}',
    'openudid':openudid,
    '_':'1510197787937',
    'callback':'Zepto1510197773887'
}

myipaddr = ('%s.%s.%s.%s' % (random.randint(1, 254), random.randint(1,254), random.randint(1, 254), random.randint(1, 254)))
headers = {
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Host':'m.jjl.cn',
    'Upgrade-Insecure-Requests':'1',
    'X-Forwarded-For': myipaddr,
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
# begin

r = requests.get(url, params=param, headers=headers)
print r.cookies.get_dict()
r.cookies.clear()
print'============Successful brush votes ! ========= \n'