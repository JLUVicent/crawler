from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.starbucks.com.cn/menu/'
# 没有ua说明不用反爬手段
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
# print(content)


soup = BeautifulSoup(content, 'lxml')

# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')
# print(name_list)
for name in name_list:
    print(name.get_text())
