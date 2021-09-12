import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# url代表下载的路径，filename代表文件名字
# 在python中可以写变量的名字，也可以直接写值
# 上面说的两个必须统一，要么都用变量名字，要么都直接写值。
# urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
# url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F7309047bf2b60563f54929c6eb5e457d03d180f12c605-Sj1plD_fw658&refer=http%3A%2F%2Fhbimg.b0.upaiyun.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1634050507&t=375789bbaf42af82d1021b7e00f58a41'

# urllib.request.urlretrieve(url_img, 'taylor.jpg')
# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-mia2yrww4rrhfp93/fhd/cae_h264_nowatermark/1631326151977910571/mda-mia2yrww4rrhfp93.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1631461397-0-0-dd9ae5510d8ceb9f534534bb62f3a2dc&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=3000187_1'

urllib.request.urlretrieve(url_video, 'quanhongchan.mp4')
