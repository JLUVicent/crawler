# 适用场景：在数据采集时候需要绕过登陆进入到某个页面
# 个人信息页面是utf-8 但是依然报错编码错误，因为没有进入到个人信息页面而是跳转到了登陆页面
# 而登陆页面不是utf-8 所以报错

# 什么时候访问不成功？
# 因为请求头的信息不够，所以访问不成功
import urllib.request

url = 'https://weibo.com/6196137410/profile'

# 反爬请求头
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': ' max-age=0',
    'cookie': ' login_sid_t=54a47350a8d7ebda333de7c35733c62e; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=6530049192105.074.1631614303406; SINAGLOBAL=6530049192105.074.1631614303406; ULV=1631614303411:1:1:1:6530049192105.074.1631614303406:; wb_view_log=1536*8641.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOUeXaMiwfrVDs6bFE_W8d5JpX5o275NHD95QceK.ceKeNSh27Ws4Dqcj_i--fi-88iKnpi--4iKL2iK.4i--Xi-zRiKn7i--NiKLFi-zXi--Ri-isiKLh; SSOLoginState=1631615130; SUB=_2A25MRAjGDeRhGeBP4lQQ8ynIyjyIHXVvMH0OrDV8PUNbmtB-LUT2kW9NRCeSIJvebc93_oZbnuDUj89jcjKQCav_; ALF=1663151130; wvr=6; wb_view_log_6196137410=1536*8641.25; UOR=,,www.baidu.com; webim_unReadCount=%7B%22time%22%3A1631617360232%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A9%2C%22msgbox%22%3A0%7D',
    'sec-ch-ua': ' "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' document',
    'sec-fetch-mode': ' navigate',
    'sec-fetch-site': ' same-origin',
    'sec-fetch-user': ' ?1',
    'upgrade-insecure-requests': ' 1',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)

print('下载成功！')
