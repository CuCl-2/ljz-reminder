# encoding:utf-8
import os
import requests
sckey=os.environ["SCKEY"]


##早上：今天在一起多少天了   天气怎么样  6:00
##晚上：一些随机的话   17:30

import requests
import time
import datetime

d2 = datetime.date(2021,5,20)
year=datetime.datetime.now().year
month=datetime.datetime.now().month
day=datetime.datetime.now().day
d1 = datetime.date(year,month,day)
days=(d1 - d2).days
msg='我已经陪伴宝贝'+str(days)+'天啦。'+'宝贝要天天开心！'


import json
import urllib.request
from urllib.parse import quote
import string
from xml.dom import minidom

def get_support_city(province):
    pass
    url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity?byProvinceName='+province
    url = quote (url, safe=string.printable)
    ret=urllib.request.urlopen(url)
    txt=ret.read().decode('utf-8')
    string_str=''
    key_value=''
    key_value_list=[]
    word_flag=0
    # print (txt)
    for i in txt:
        string_str += i
        # print(string_str)
        if string_str.replace(' ','').replace('\t','').replace('\n','').replace('\r','')== '<string>':
            # print ('---------------------------string_str')
            word_flag = 1
        if i=='>':
            string_str=''
        if word_flag==1:
            key_value+=i
            # print(key_value,'*************************************')
        else:
            key_value=''
        if i=='<' and word_flag==1:
            key_value_list.append(key_value.replace('<','').replace('>','').replace('(','').replace(')',''))
            key_value=''
            word_flag=0
    # print(key_value_list)
    support_city={}
    for i in key_value_list:
        # print(i)
        word=i.split(' ')
        support_city[word[0]]=word[1]
    # print(support_city)
    return support_city
#（2）获取天气
def get_weather(name):
    page = urllib.request.urlopen("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName="+name)
    lines = page.readlines()
    page.close()
    document = ""
    for line in lines :
        document = document + line.decode('utf-8')

    from xml.dom.minidom import parseString
    dom =parseString(document)
    strings = dom.getElementsByTagName("string")
    return strings[10].childNodes[0].data

province='浙江'
province = quote (province, safe=string.printable)
support_city=get_support_city(province)
name='杭州'
# name = quote (name, safe=string.printable)
name=support_city[name]
tianqi = get_weather (name)[7:]



saohua=['记得想我噢','宝贝说过要对我好的，我也会对宝贝好的','宝贝说对我的爱不会消失的','我会一直陪着宝贝的','宝贝是最棒的！'
    ,'你知道你和星星有什么区别吗？星星在天上，你在我心里。','我觉得你特别像一款游戏——我的世界','你有打火机吗？没有。那为什么还能点燃我的心？',
        '我要出去下，去哪里？去寻找我们的未来。','你会喜欢我吗？不会我教你啊。','你可以帮我洗个东西吗 ？喜欢我。',
        '我房租到期了，可以去你心里住吗？','苦海无涯，回头是我。','如果不能一夜暴富，一夜抱你也行。']
length=len(saohua)
import random
index=(random.randint(0, length-1))

now = time.asctime(time.localtime(time.time()))
shijian = now[11:13]
print('时间'+shijian)
if(shijian=='22'):
    print(msg)
    requests.post('http://sc.ftqq.com/' + sckey + '.send', data={'text': msg, 'desp': ""})
    print(tianqi)
    requests.post('http://sc.ftqq.com/'+sckey+'.send', data={'text': tianqi, 'desp': ""})
if(shijian=='09'):
    print(saohua[index])
    requests.post('http://sc.ftqq.com/' + sckey + '.send', data={'text': saohua[index], 'desp': ""})






