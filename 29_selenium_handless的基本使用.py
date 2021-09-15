# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('‐‐headless')
# chrome_options.add_argument('‐‐disable‐gpu')
# # path路径是自己电脑浏览器的路径文件
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
# browser = webdriver.Chrome(chrome_options=chrome_options)


# url = 'https://www.baidu.com'
# browser.get(url)

# # 拍个照片
# browser.save_screenshot('baidu.png')

# 封装的handless

# 无界面浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    # path路径是自己电脑浏览器的路径文件
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser()
url = 'https://baidu.com'
browser.get(url)
