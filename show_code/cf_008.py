#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'http://v3.bootcss.com/'

req = requests.get(url)
r = req.text.encode('ISO-8859-1', errors='ignore').decode('utf-8', errors='ignore')

soup = BeautifulSoup(r, "lxml")
# print(soup.body)
print(soup.find_all('img'))
for i in soup.find_all('img'):
    print(i['src'])

s = '北京是个好城市'
print(s.replace('北京', '{}'.format('*' * len('北京'))))
