

import json
import jsonpath

# 书店所有书的作者
obj = json.load(open('20_解析_jsonpath.json', 'r', encoding='utf-8'))
# print(obj)
# book后面有个通配符*用来表示所有书，若为0表示第一本书，以此类推。
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')


# # 所有的作者 注意和上面的区别
# author_list = jsonpath.jsonpath(obj, '$..author')


# print(author_list)

# store下面的所有元素
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# store所有东西的price
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)

# 第三本书
# book = jsonpath.jsonpath(obj, '$..book[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(book)

# 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)

# 条件过滤需要在()前面添加?
# 过滤出所有包含版本号isbn的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list)

# 哪本书超过了10块
book_list = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book_list)
