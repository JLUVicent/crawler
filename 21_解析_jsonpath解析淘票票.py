
import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1631671969386_137&jsoncallback=jsonp138&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': ' cna=orx3Gb1BbSQCASQpl/dgXzJE; UM_distinctid=17aaca72d93b4-089d53faebdb4a-6373264-144000-17aaca72d94774; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; t=e63ba96e69bb428d133672981c9bd7f9; _m_h5_tk=8c565c5365f3e8ee6bb33008bac6689a_1631638268258; _m_h5_tk_enc=e4de286ea35e05813d236a1e12390dca; xlly_s=1; cookie2=11e748f07397f86a00ae7f6d7bd83dd7; v=0; _tb_token_=3e37ef70fe77e; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=ccxVBN1aumnq7ISsJisZcQaMDo7AZp5GOuWFoU3RJDdTcMbciYPOEFrlUO5KqZf..; l=eBOPt3KegaUZM7hFBO5aourza77TNIRb8sPzaNbMiInca6pCtFNjZNCLGYmpSdtjgt5F7eKrd8LeqREDzfa_WdsWHpfk_OEyACJ68e1..; isg=BLy8yYXn8Q7E6MU65MFv8Q4rjVputWDfghCpd5Y9YaeKYV3rv8CsbV3fQYkZKZg3',
    'referer': ' https://dianying.taobao.com/index.htm?spm=a1z21.3046609.header.3.6d26112apwuljH&n_s=new',
    'sec-ch-ua': ' "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'x-requested-with': ' XMLHttpRequest',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据
content = response.read().decode('utf-8')

# split 切割 得到想要的json数据
content = content.split('(')[1].split(')')[0]


with open('21tpp.json', 'w', encoding='utf-8')as fp:
    fp.write(content)

obj = json.load(open('21tpp.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)
