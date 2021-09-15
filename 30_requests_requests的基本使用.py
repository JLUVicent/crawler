
import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
# print(type(response))

# 设置响应的编码格式
# response.encoding = 'utf-8'

# 以字符串形式返回网页源码***常用
# print(response.text)

# 返回url地址
# print(response.url)

# 返回二进制的数据源码：用的不多
# print(response.content)

# 返回响应的状态码  正确为200
# print(response.status_code)

# 获取响应头
# print(response.headers)
