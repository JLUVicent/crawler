
import time
from selenium import webdriver

path = 'phantomjs.exe'

browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'

browser.get(url)

# 拍快照
browser.save_screenshot('baidu.png')

time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('Vicent')
time.sleep(2)
browser.save_screenshot('Vicent.png')
