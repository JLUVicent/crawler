
# 通过登陆   进入到主页面


# 通过找登陆接口发现登陆时候需要的参数很多在login中找

# __VIEWSTATE: kBeYlQh4JeI1J7uQdLrUffn6FHUW2mJE8dKQYKQypdnw4kIi6ZE63qg6WoLKkbeVKkpzY+XGF3E2dB/e4nViUEKrd7gvgC4uyMiNOUcKptmPrYXxO0hgkpyZhIQ=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 17390955615@163.com
# pwd: 1233312
# code: z0x6
# denglu: 登录

# 观察到__VIEWSTATE， __VIEWSTATEGENERATOR，以及code是变化的


# 难点：（1）__VIEWSTATE， __VIEWSTATEGENERATOR  一般情况下看不到的数据都在页面的源码中
#      观察到两个数据在页面的源码中，因此我们需要获取页面的源码然后进行解析就可以了
#      （2）验证码
import urllib.request
from bs4 import BeautifulSoup
import requests

# 登陆页面的Url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 获取页面的源码
response = requests.get(url=url, headers=headers)
content = response.text

# print(content)

# 解析页面源码获取__VIEWSTATE， __VIEWSTATEGENERATOR的值


soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR的值
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')


# 获取验证码图片

code = soup.select('#imgCode')[0].attrs.get('src')
# print(code)

code_url = 'https://so.gushiwen.cn'+code
# print(code_url)

# 有坑
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')

# requests里面有一个方法交session(),通过session的返回值就能使得请求变成对象
session = requests.session()
# 验证码的url的内容
response_code = session.get(code_url)
# 注意此时要使用二进制数据，因为我们要使用图片的瞎子啊
content_code = response_code.content
# wb模式是将二进制数据写入文件
with open('code.jpg', 'wb')as fp:
    fp.write(content_code)

# 获取验证码的图片之后下载到本地观察验证码在控制台输入验证码可以将值赋给code参数
code_name = input('请输入你的验证码:')

# 点击登录

url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '17390955615@163.com',
    'pwd': '2bldhbfh',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8')as fp:
    fp.write(content_post)
