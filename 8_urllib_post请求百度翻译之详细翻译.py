import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': ' */*',
    # 'Accept-Encoding': ' gzip, deflate, br',
    # 'Accept-Language': ' zh-CN,zh;q=0.9,en;q=0.8',
    # 'Connection': ' keep-alive',
    # 'Content-Length': ' 116',
    # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    # 在网页中找到requests头文件来解决反爬问题
    'Cookie': ' BIDUPSID=3355538E657F8F485205070E5E6B53B4; PSTM=1625971471; BAIDUID=3355538E657F8F483B76E75C6D5C203A:FG=1; __yjs_duid=1_1665433ddae7605c2348afb1bc971dd61626186695679; BDUSS=UM3V1FlY0h-OElPWVJWbXdBZX51a2o2ejAxVE9IQmtsTk4wSVVEUnRhR24yUmhoRVFBQUFBJCQAAAAAAAAAAAEAAADMK6KaMjA4MMrVMjA4MHRpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKdM8WCnTPFgW; BDUSS_BFESS=UM3V1FlY0h-OElPWVJWbXdBZX51a2o2ejAxVE9IQmtsTk4wSVVEUnRhR24yUmhoRVFBQUFBJCQAAAAAAAAAAAEAAADMK6KaMjA4MMrVMjA4MHRpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKdM8WCnTPFgW; H_PS_PSSID=31253_26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[shF0fZW8Lss]=mk3SLVN4HKm; delPer=0; PSINO=6; BAIDUID_BFESS=057D6840C1E3792FE79EF62955977783:FG=1; BA_HECTOR=218l000lagaga501cn1gju4mu0q; BCLID=8746547366435560005; BDSFRCVID=nZ-OJexroG0YyvRHhTlsejgZQFweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKy2OTH9LF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF30pjbXP6-hnjy3bRkX4Q4WnnzVJrNM4JA0fKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURv2jDg3-A8WU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhRCLWMT-MTryKKJwM4QCObn2hbbqM4-l0tjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPU2H59LUk8Bgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D_9e5LK3e; BCLID_BFESS=8746547366435560005; BDSFRCVID_BFESS=nZ-OJexroG0YyvRHhTlsejgZQFweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKy2OTH9LF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF30pjbXP6-hnjy3bRkX4Q4WnnzVJrNM4JA0fKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURv2jDg3-A8WU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhRCLWMT-MTryKKJwM4QCObn2hbbqM4-l0tjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPU2H59LUk8Bgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D_9e5LK3e; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1631521272,1631522248,1631523552,1631523563; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1631523563; __yjs_st=2_M2I2YzkyMTBjYmM2Yzg4NDMxZGE2MmUzM2UzMWQ3MTA1MzgwZmFkMGI3ZTVhNjljNzIyZDlkYjBkMjcwNmQzZTYyNWI2MmQ3OWFlOGE3YWY3YzlkYmEzZWU4NGJhZjQxZGNiMTA5NjM2YmExM2NmNzliN2ZkZTMxMmVhNTI2ODQzZGMzYWJmYzZhYzBhZDcwNzQ0ODYwY2MyYWMyOGNlNzQyNTg0ZmU0NDY0ZDVhYjQ5ZjM4MDNhYTc5NjBjMjhmN2JlNTgzOGE3NmQ4YmIxMzhkOTg4OTUyZjE4ZDU5MGJkNDk2NjRiNjBmNjMwNWQ3ZGM5OTJiMGM1YWQ3ZjcyYl83XzI1YWVhYTk5; ab_sr=1.0.1_OWQ3NzkxMjliMTc4ZmNjMmQzNTM5MmIyZDIyNTg1YzU2ZjA4N2I5Mjc4MWZiYzRkMTQ1NzdlODA2YmVlMDIyMmI2ZjgyMzQwODFiOTBkYzYyNjcwNTdlZTJiYmFmNzdlODdjYmRhNzA1YjVkZmMwYjA4OWI2MTk5YzUzNTc2ZjA5ZWQ1NWJhZmZlMGNjN2M3Yjc0MDZiZjZiM2E0NzhmNWIwMjNjNDZmMzg1MWEwNDRiZDVjMDY0ZmM1NmRiMTNm',
    #     'Host': ' fanyi.baidu.com',
    #     'Origin': ' https://fanyi.baidu.com',
    #     'Referer': ' https://fanyi.baidu.com/?aldtype=16047',
    #     'sec-ch-ua': ' "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    #     'sec-ch-ua-mobile': ' ?0',
    #     'sec-ch-ua-platform': ' "Windows"',
    #     'Sec-Fetch-Dest': ' empty',
    #     'Sec-Fetch-Mode': ' cors',
    #     'Sec-Fetch-Site': ' same-origin',
    #     'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    #     'X-Requested-With': ' XMLHttpRequest',
}

# 这有个小bug找了好久，注意直接复制过来有空格，要把空格去掉。当时en前面有空格，无法输出，一定要注意！！！
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '9811d3400c4dee324641f2cc9ad7f55b',
    'domain': 'common',
}

# post请求的参数必须进行encode编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求参数，不会拼接在url后面，需要进行请求对象参数定制
request = urllib.request.Request(url=url,  data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

# 字符串-->json对象
obj = json.loads(content)
print(obj)
