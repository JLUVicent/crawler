1.创建爬虫的项目：scrapy startproject 项目名字
                注意：项目名不允许使用数字开头，不能包含中文
2.创建爬虫文件：  要在spiders文件夹中去创建爬虫文件
                cd 项目的名字\项目的名字\spiders
                cd scrapy_baidu_036\scrapy_baidu_036\spiders
                

                创建爬虫文件
                scrapy genspider 爬虫文件的名字 要爬取的网页
                eg:scrapy genspider baidu http://www.baidu.com
                一般情况下不需要添加http协议，因为start_urls的值是根据allowed_domains
                修改的，因此添加了http话，start_urls的值需要我们手动修改

3.运行爬虫代码
                scrapy crawl 爬虫的名字
                eg：scrapy crawl baidu