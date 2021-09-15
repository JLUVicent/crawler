

# （1）请求对象的定制
# （2）获取网页的源码
# （3）下载


# 需求  下载前十页的图片
import urllib.request
from lxml import etree
# https://sc.chinaz.com/tupian/qinglvtupian.html（第一页）
# https://sc.chinaz.com/tupian/qinglvtupian_2.html（第二页）
# https://sc.chinaz.com/tupian/qinglvtupian_3.html（第三页）


def creat_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    # 下载图片
    # urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # 一般涉及图片的网站都会进行懒加载，因此需要使用src2来进行
    img_url = tree.xpath('//div[@id="container"]//a/img/@src2')
    for i in range(len(name_list)):
        name = name_list[i]
        img = img_url[i]
        url = 'https:'+img
        urllib.request.urlretrieve(url=url, filename='./love_img/'+name+'.jpg')


if __name__ == '__main__':
    start_page = int(input("请输入起始页："))
    end_page = int(input("请输入终止页："))
    for page in range(start_page, end_page+1):
        # (1)请求对象的定制
        request = creat_request(page)
        # (2)获取网页源码
        content = get_content(request)
        # (3)下载
        down_load(content)
