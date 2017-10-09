#!/usr/bin/python
# -*- coding:utf-8 -*-
l = ['112.13.54.66',
     '112.13.54.40',
     '112.13.54.1',
     '112.13.54.13',
     '112.13.54.73',
     '127.0.0.1',
     '218.189.25.130']
# import requests
#
# payload = {'ip': '112.13.54.73', 'ak': 'I2hMl7KTELnsvRaEDFK0eGp6jOTC0Clj'}
# url = requests.get('http://api.map.baidu.com/location/ip', params=payload)
# data = url.json()
# print(data)

# l = ['a','b']
# print(dict(l))
# import random
# import time
import requests

# n = 20
# while True:
#     with open(r'E:\MyProject\deploy\access1.txt', 'a+', encoding='utf-8') as file:
#         file.write(
#             "INSERT INTO `blog`.`users` (`id`, `username`, `password`, `email`, `avatar`, `status`, `is_valid`, `confirmed`, `confirmed_on`, `created_at`, `updated_at`, `last_login`, `post_total`, `role`, `wx_img`, `zfb_img`, `wx_num`, `zfb_num`, `city`, `county`, `ip_addr`, `region`, `area`) VALUES ('{0}', 'asfedfg{1}', 'pbkdf2:sha1:1000$2wjyCWot$bd717db744c7a684aaf1075e5e8f7efd7e11832a', 'asssdfg{2}@qq.com', '/static/avatar/default_avatar.png', '1', '1', '1', '2017-04-17 21:23:25', '2017-04-17 21:22:53', '2017-04-17 21:22:53', '2017-04-18 23:31:53', '0', '0', '/static/wximg/wx_300_1.99.png', '/static/zfbimg/zfb_300_1.99.png', '1.99', '1.99', '{3}', '', '', '', '');".format(
#                 n, n, n, random.choice(['温州', '上海', '广州', '北京', '重庆', '天津', '十堰'])) + '\n')
#         n = n + 1
#         print('ok', n)
#         time.sleep(1)
#         if n == 300:
#             print('完成')
#         break

r = requests.get('https://www.51qinqing.com/static/images/404.png',
                 headers={'Referer': 'https://www.51qinqfging.com'})
print(r.request.headers)
with open('1.png', 'wb') as f:
     f.write(r.content)