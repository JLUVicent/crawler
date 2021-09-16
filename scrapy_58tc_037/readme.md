1.scrapy项目的结构
    项目名字
        项目名字
            spiders文件夹(存储的是爬虫文件)
                init
                自定义的爬虫文件        核心功能文件************最重要的
            init
            items           定义数据结构的地方 爬取的数据包含哪些
            middlewares     中间件            代理
            pipelines       管道              用来处理下载的数据
            settings        配置文件          robots协议 ua定义


2.response的属性和方法
    response.text       获取响应的字符串
    response.body       获取二进制数据
    response.xpath      可以直接使用xpath方法来解析response中的内容
    response.extract()  提取selector对象的data属性值
    response.extract_first()    提取的是selector列表的第一个数据