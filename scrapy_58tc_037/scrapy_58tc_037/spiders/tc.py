import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = [
        'https://wn.58.com/job/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = [
        'https://wn.58.com/job/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/']

    def parse(self, response):
        # print('山东菏泽曹县')
        # 获取字符串
        # content = response.text
        # 获取二进制数据
        # content = response.body

        print('================')
        # print(content)

        span = response.xpath('//div[@id="filterJob"]//li[@class="select"]')[0]
        print(span.extract())
        # print(span)
