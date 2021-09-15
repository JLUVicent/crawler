from bs4 import BeautifulSoup

# 解析本地文件介绍基础的bs4语法
# 默认打开文件的编码格式是GBK，所以在打开文件时候需要制定编码
soup = BeautifulSoup(open('22_解析_bs4的基本使用.html',  encoding='utf-8'), 'lxml')
# print(soup)

# 根据标签名查找节点
# 找到的是第一个符合条件的数据
# print(soup.a)

# #获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# (1)find
# 返回的是第一个符合条件的数据
# print(soup.find('a'))

# 根据title的值找到对应的标签对象
# print(soup.find('a', title="a2"))

# 根据class的值来找到对应的标签对象   注意：class是关键字需要添加下划线
# print(soup.find('a', class_="a1"))


# (2)find_all
# 返回的是一个列表并且反悔了所有的a标签
# print(soup.find_all('a'))

# 如果获取多个标签数据，需要在find_all中添加的是列表的数据
# print(soup.find_all(['a', 'span']))

# limit作用是查找前几个数据
# print(soup.find_all('li', limit=2))


# (3)select

# select方法返回一个列表并且返回多个数据
# print(soup.select('a'))

# 可以通过.代表class，这种操作叫做类选择器
# print(soup.select('.a1'))

# 用#号代表id
# print(soup.select('#l1'))

# 属性选择器-->通过属性来寻找对应的标签
# 查找到li标签中有id的标签
# print(soup.select('li[id]'))

# 查找li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# 找到的是div下面的li
# 空格表示后代
# print(soup.select('div li'))

# 子代选择器
# 某标签的第一级子标签
# >表示子代
# 注意：很多的计算机编程语言中如果不加空格不会输出内容，但是在bs4中不会报错
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有的对象
# print(soup.select('a,li'))


# 节点信息

# 获取节点内容
obj = soup.select('#d1')[0]
# # 如果标签对象中只有内容，则string和get_text都可以使用
# # 如果标签对象中，除了内容还有标签，则string不能用，get_text能获取到标签
# # 一般情况下使用get_text()
# print(obj.string)
# print(obj.get_text())


# 节点的属性
obj = soup.select('#p1')[0]
# name是标签的名字
print(obj.name)
# 将属性值作为字典返回
print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))

print(obj.get('class'))

print(obj['class'])
