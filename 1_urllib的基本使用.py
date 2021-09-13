# 使用urllib来获取百度首页源码

# （1）定义一个url,就是要访问的地址
import urllib.request
url = 'http://www.baidu.com'

# （2）模拟浏览器向服务器发送请求 response响应
response = urllib.request.urlopen(url)

# （3）获取响应中的页面源码
# read方法 返回字节形式的二进制数据
# 将二进制数据转换为字符串
# 二进制--》字符串 解码 decode('编码的格式')
content = response.read().decode('utf-8')


# （4）打印数据
print(content)
