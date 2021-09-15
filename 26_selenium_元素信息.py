from selenium import webdriver


path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

# 找id返回的不是一个列表
input = browser.find_element_by_id("su")
# 获取标签的属性对应值
print(input.get_attribute('class'))
# 获取标签名
print(input.tag_name)
# 获取元素文本 获取两个尖括号之间的数据
a = browser.find_element_by_link_text('新闻')
print(a.text)
