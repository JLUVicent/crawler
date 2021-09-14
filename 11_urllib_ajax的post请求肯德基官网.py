# 第1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 如何判断是ajax：看核心对象：X-Requested-With:XMLHttpRequest
# 第2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post请求
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

# 不同的页数其中的pageIndex不同

# 通常接口寻找比较麻烦

import urllib.request
import urllib.parse


def creat_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    # post请求的参数必须要编码
    data = urllib.parse.urlencode(data).encode('utf-8')

    # 反爬请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    # 定制
    request = urllib.request.Request(url=base_url, headers=headers, data=data)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('k'+str(page)+'fc'+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page, end_page+1):
        # 请求对象的定制
        request = creat_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(page, content)
