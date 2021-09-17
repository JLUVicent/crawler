import scrapy
import json


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['https://fanyi.baidu.com/sug']
    # post请求如果没有参数则没有任何意义
    # 因此start_urls没有用了
    # 所以parse方法也没有用了
    # start_urls = ['https://fanyi.baidu.com/sug/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'final'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)
