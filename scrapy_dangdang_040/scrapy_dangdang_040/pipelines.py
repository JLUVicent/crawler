# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想要使用管道必须在settings中开启管道


class ScrapyDangdang040Pipeline:
    # 爬虫文件开始之前就执行的方法，执行一次
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')
    # item就是yield后面的book对象
    # 以下这种模式不推荐，因为每传递一个对象，那么就打开一个文件，对文件操作太频繁
    # def process_item(self, item, spider):
    #     # （1）write方法必须要写一个字符串不能是对象
    #     # （2）w模式会每一个对象都打开一次文件，覆盖之前的内容然后关闭，因此需要写a
    #     with open('book.json', 'a', encoding='utf-8')as fp:
    #         fp.write(str(item))

    def process_item(self, item, spider):
        self.fp.write(str(item))

        return item
    # 在爬虫文件执行完之后执行的方法执行一次

    def close_spider(self, spider):
        self.fp.close()
