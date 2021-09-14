
# 需求：使用handler来访问百度 获取网页源码

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# handler     build_opener     open

# 下面三步就相当于这条命令urllib.request.urlopen(request)
# 使用下面命令可以使用一些代理ip来进行访问
# （1）获取handler对象
handler = urllib.request.HTTPHandler()

# （2）获取opener对象
opener = urllib.request.build_opener(handler)

# （3）调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
