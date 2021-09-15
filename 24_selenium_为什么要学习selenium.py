import urllib.request

# 虽然爬取到了页面但是没有找到我们想要的东西
# 需要使用selenium实现动态加载

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
