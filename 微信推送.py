# import requests
# import json
# token = '136676865ab44375bba871dd0f9ea425' #在pushpush网站中可以找到
# title= '打卡成功' #改成你要的标题内容
# content ='地点：浙江杭州 时间' #改成你要的正文内容
# url = 'http://www.pushplus.plus/send'
# data = {
#     "token":token,
#     "title":title,
#     "content":content
# }
# body=json.dumps(data).encode(encoding='utf-8')
# headers = {'Content-Type':'application/json'}
# requests.post(url,data=body,headers=headers)


# encoding:utf-8
import os

import requests
token = os.environ["token"] #在pushpush网站中可以找到
title= '打卡成功' #改成你要的标题内容
content ='地点：浙江杭州 时间' #改成你要的正文内容
url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
requests.get(url)




import requests
sckey=os.environ["sckey"]
requests.post('http://sc.ftqq.com/'+sckey+'.send', data={'text': "打卡成功", 'desp': ""})
