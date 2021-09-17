import scrapy


class LogSpider(scrapy.Spider):
    name = 'log'
    allowed_domains = ['www.bidu.com']
    start_urls = ['http://www.bidu.com/']

    def parse(self, response):
        # pass
        print("+++++++++++++++++++++++++++")
