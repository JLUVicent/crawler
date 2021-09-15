from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

#
url = 'https://www.baidu.com'
browser.get(url)

# 元素定位

# # （1）根据id找到对象*********常用
# button = browser.find_element_by_id('su')
# print(button)

# （2）根据标签属性的属性值获取对象
# button = browser.find_element_by_name('wd')
# print(button)

# （3）id是唯一的，根据xpath语句获取对象******常用
# button = browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)

# （4）根据标签名获取对象
# button=browser.find_elements_by_tag_name('input')
# print(button)

# （5）使用bs4的语法来实现******常用
# button = browser.find_element_by_css_selector('#su')
# print(button)

# （6）通过页面的链接定位文本
# button=browser.find_element_by_link_text('直播')
# print(button)
