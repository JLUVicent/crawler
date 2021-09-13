# 首先抓接口

# get请求
# 获取豆瓣电影的第一页数据并且保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# （1）请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# （2）获取响应的数据
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
# print(content)

# （3）数据下载到本地,如果是json数据就保存成json格式
# open方法默认情况使用GBK编码，如果要保存汉字，需要在open方法中指定编码格式为utf-8
# encoding='utf-8'
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)
with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
