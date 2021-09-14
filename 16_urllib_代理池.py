# 随机调用代理池中的Ip进行访问

import random
import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

# 代理ip不稳定，如需要代理ip则要购买，这里展示代理池的用法。
proxis_pool = [
    {'http': '211.65.197.93:80'},
    {'http': '211.65.197.93:80'}
]


proxis = random.choice(proxis_pool)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# print(proxis)

# 用代理必须用下面三个获取响应
handler = urllib.request.ProxyHandler(proxies=proxis)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('dailipool.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
