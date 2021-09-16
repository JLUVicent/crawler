import scrapy
from scrapy_dangdang_040.items import ScrapyDangdang040Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    def parse(self, response):
        print("-----------------------------")

        # pipelines  下载数据
        # items      定义数据结构

        # src='//ul[@id="component_59"]/li//img/@src'
        # alt='//ul[@id="component_59"]/li//img/@alt'
        # price='//ul[@id="component_59"]/li//span[@class="search_now_price"]/text()'
        # 所有的seletor的对象都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 图片有懒加载，需要注意更换路径
            # 第一张图片和其他标签的属性是不一样的
            # 第一张图片的src可以使用，其他的图片的地址是data-original
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath(
                './/span[@class="search_now_price"]/text()').extract_first()

            book = ScrapyDangdang040Item(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book
        pass
