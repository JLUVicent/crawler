
# （1）获取网页的源码
# （2）解析      解析的服务器响应的文件  etree.HTML
# （3）打印

from lxml import etree
import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 另外一种模拟浏览器的方式
# 走代理池
# import random
# #里面是代理
# proxies_poll=[
# {}
# {}
# ]
# proxies=random.choice(proxies_poll)

# handler=urllib.request.ProxyHandler(proxies=proxies)
# opener=urllib.request.build_opener(handler)
# response=opener.open(response)

# 得到数据
content = response.read().decode('utf-8')
# print(content)

# 解析网页源码获取需要的数据

# 解析服务器响应的文献
tree = etree.HTML(content)

# 获取想要的数据 Xpath返回的就是列表类型
# xpath括号中的内容在浏览器中xpath插件中可以得到
# 如果不让返回列表，直接返回其索引值即可
# //*[@id="su"]
# result = tree.xpath('//input[@id="su"]/@value')[0]
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)
print(type(result))
