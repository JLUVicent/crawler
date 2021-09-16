
import requests
from requests.models import encode_multipart_formdata

url = 'http://www.baidu.com/s?'
data = {
    'wd': 'ip'
}

proxy = {
    'http://': '27.156.197.17:4235'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)

content = response.text

with open('adaili.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
