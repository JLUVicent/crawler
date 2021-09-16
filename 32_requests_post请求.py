

import json
import requests
from requests.models import encode_multipart_formdata

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

data = {
    'kw': 'eye'
}

# url 请求地址
# data 请求参数
# kwargs 字典
response = requests.post(url=url, data=data, headers=headers)

content = response.text
print(content)

obj = json.loads(content)
print(obj)

# 总结：
# （1）post请求不需要编解码
# （2）post请求的参数是data
# （3）不需要请求对象的定制
