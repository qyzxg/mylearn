#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import uuid
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#
# r = requests.get('http://www.meizitu.com/a/5500.html', headers=headers)
#
# soup = BeautifulSoup(r.text,'html.parser')
# u = soup.find('div', class_="postContent").find_all('img')
# for i in u:
#     print(i['src'])

def meizi(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    proxies = {"http": "http://61.160.190.34:8888"}
    print(url)
    try:
        r = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(r.text, 'html.parser')
        imgu = soup.find('div', id="picture").find_all('img')
        for j in imgu:
            print('正在下载:', j['src'])
            src = requests.get(j['src'], headers=headers, proxies=proxies)
            _dir = os.path.join(os.getcwd(), 'meizitu')
            filename = str(uuid.uuid1()) + '.jpg'
            fpath = os.path.join(_dir, filename)
            with open(fpath, 'wb') as file:
                file.write(src.content)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    p = Pool(12)
    for i in range(3525, 5547):
        url = 'http://www.meizitu.com/a/{}.html'.format(i)
        p.apply_async(meizi, args=(url,))
    p.close()
    p.join()
    print('下载完成')
