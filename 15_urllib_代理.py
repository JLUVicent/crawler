import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)
# handler build_opener open

# 这个代理不太好使，得买代理
proxies = {
    'http': '117.88.246.51:3000'
}

# ProxyHandler中是一个以字典形式存在的代理ip
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

# 获取响应信息
content = response.read().decode('utf-8')

# print(content)

# 保存
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
