import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行爬虫的时候使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']

    # 起始的url地址 第一次要访问的域名
    # start_urls是在allowed_domains的前面添加http://,在allowed_domains后面添加/
    start_urls = ['http://www.baidu.com/']
    # 执行了start_urls之后执行的方法，方法中的response就是返回的对象
    # 相当于response=urllib.request.urlopen(url)
    # 相当于response=request.get(url)

    def parse(self, response):
        print('我在爬爬爬')
        pass
