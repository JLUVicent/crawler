import re
import scrapy
from scrapy_move_041.items import ScrapyMove041Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    # 允许访问路径一般都写域名就行了
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一页的名字和第二页的图片

        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            # 获取第一页的name和要点击的连接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'https://www.ygdy8.net'+href
            # print(name, href, url)

            # 对第二页的连接发起访问

            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # print('123456')
        # 注意：如果拿不到数据，要检查xpath语法是否正确
        # //div[@id="Zoom"]//span//img/@src其中的span无法识别，需要删除
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # print(src)
        # print(type(src))
# 接受到请求的那个Meta的参数的值
        name = response.meta['name']
        # # print(src)
        # print(name)
        # print(type(name))

        movie = ScrapyMove041Item(src=src, name=name)

        yield movie
