import requests
from  requests import Session
from bs4 import BeautifulSoup


def cruise_urls():
    root = 'http://www.tapotiexie.com'
    result = []
    for n in range(1, 26):
        html = requests.get(
            url='http://www.tapotiexie.com/Line/index/name/yt/port/0/mouth/0/company/0/p/{}.html'.format(n))
        soup = BeautifulSoup(html.text, 'lxml')
        for i in soup.find_all(class_='tptx_jcyj_2ac_2'):
            result.append(root + i.a.get('href'))
    return result

for i in cruise_urls():
    print(i)

print(len(cruise_urls()))