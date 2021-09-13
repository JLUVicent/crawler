# post请求
import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

# 反爬请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 写入数据
data = {
    'kw': 'spider'
}

# post请求的参数必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)

# post的请求参数 是不会拼接在url后面的 而是需要放在请求对象定制的参数中
# post请求的参数必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

# 字符串--》json对象

obj = json.loads(content)
print(obj)

# post请求方式的参数必须编码
# 编码之后必须调用encode方法
# 参数是放在请求定制的方法中
