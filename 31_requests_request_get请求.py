# urllib知识梳理，对比来记忆
# （1）一个类型六个方法
# （2）get请求     quote urlencode
# （3）post请求    百度翻译
# （4）ajax的get请求
# （5）ajax的post请求
# （6）cookie登陆   微博直接进入个人页面
# （7）代理         快代理

# requests
# （1）一个类型六个属性
# （2）get请求
# （3）post请求
# （4）代理
# （5）cookie 破解验证码
import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

data = {
    'wd': '北京'
}

# url 请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)

content = response.text

print(content)

# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象的定制
# 请求资源路径中的?可以省略
