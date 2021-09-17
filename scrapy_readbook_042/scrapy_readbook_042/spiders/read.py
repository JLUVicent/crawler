import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_042.items import ScrapyReadbook042Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    # 注意开始页，需要在1617后面加上_1
    start_urls = ['https://www.dushu.com/book/1617_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1617_\d+\.html'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        # item = {}
        # print("+++++++++++++++++")
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()

            # print(name, src)
            book = ScrapyReadbook042Item(name=name, src=src)
            yield book
