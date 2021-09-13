import urllib.request

url = 'https://www.baidu.com'

# URL的组成
# https://www.baidu.com/s?tn=59044660_hao_pg&ie=utf-8&wd=周杰伦
#http/https     www.baidu.com   80/443      s         wd=周杰伦 #
# 协议           主机             端口号      路径      参数      锚点
# http 80
# https 443
# mysql 3306
# oracle 1521
# redis 6379
# mongodb 27017
# headers内容在浏览器中点击检查-network-刷新-看域名-到最下面
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# 因为urlopen方法中不能存储字典，所以headers不能传递出去
# 请求对象的定制
# 注意 因为参数顺序的问题，不能直接写url和headers 中间还有data 所以我们需要关键字传参
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
