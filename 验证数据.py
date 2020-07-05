# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:56:00 2020

@author: dell
"""

# 爬取验证数据
url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage'
response=requests.get(url).text
data=re.findall('({"confirmed":".*?","died":".*?","crued":".*?","relativeTime".*?),"subList"',response)[:34] # 提取信息
data=[i+'}' for i in data]
for i in data:
    i=json.loads(i)
    ne=i['area']  # 疫情地区
    to_ad=i['confirmedRelative']  # 新增
    contrast[ne]=to_ad