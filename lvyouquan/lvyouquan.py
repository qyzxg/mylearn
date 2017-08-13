#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import time
import requests
import json

print(time.time())
user_name = "pzx4@qq.com"
pass_word = 'Answer'
mobile_num = '13777793289'
headers = {
    'Host': 'lyqapp.lvyouquan.cn',
    'sign': 'C5QudFvQQMO5scYhul5Fd2oSpmh7DigzQYXGx4vEVd1T6td4OrcIiofLyDv2xPh1rscLemeMOEnRXsQU3iAK7g==',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'ShouKeBao/2.4.21 (iPhone; iOS 10.3.3; Scale/3.00)',
    'MobileVersion': '2.4.2',
    'Cookie': 'SERVERID=web34',
    'Content-Length': '377'
}
login_data = {"Mobile": "13777793289", "MobileID": "4B891ECB-80C2-458F-A8AD-A12E3BF2FFE3", "Substation": "10",
              "BusinessID": "9d760a70aadc4b4a979e95fd35a3e1e6", "ClientSource": "2", "MobileVersion": "2.4.2",
              "StartCityId": "10", "AppUserID": "e4313d21f3b24e0da730da03eb4cb4c2", "MobileType": "1",
              "systemVersion": "10.3.3", "LoginPassword": "Answer", "DistributionID": "", "LoginType": "1"}

root_url = 'http://lyqapp.lvyouquan.cn'
login_url = root_url + '/Business/LoginDistributor'
mobile_url = root_url + '/Business/LoginQuick'
session = requests.Session()
r = session.post(url=mobile_url, headers=headers, data=json.dumps(login_data))
print(r.text)

