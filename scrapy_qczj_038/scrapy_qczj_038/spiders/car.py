import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    # 注意如果请求接口后缀为html时候，不需要加/，加/报错
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        # print('我来汽车之家爬爬爬了')
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        # print(name_list)
        price_list = response.xpath(
            '//div[@class="main-lever"]//span/span/text()')

        for i in range(len(name_list)):
            # extract()提取data数据
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)

        # pass
