# urlencode应用场景：多个参数的时候

# https://www.baidu.com/s?tn=59044660_hao_pg&ie=utf-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# import urllib.parse
# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location':'中国台湾省'
# }

# a = urllib.parse.urlencode(data)
# print(a)

# 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE的网页源码

import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url+new_data

# 防止反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

print(content)
