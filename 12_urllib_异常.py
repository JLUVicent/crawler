# https://blog.csdn.net/qq_38998213/article/details/120255800
import urllib.request
import urllib.error
# url = 'https://blog.csdn.net/qq_38998213/article/details/120255800'

url = 'https://blog.csdn.net/qq_38998213/article/details/1202558001'
# 反爬请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

try:

    # 请求对象定制
    request = urllib.request.Request(headers=headers, url=url)

    # 模拟浏览器发送请求
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('爬虫学得好，监狱进的早！')

except urllib.error.URLError:
    print('链接有误！')
