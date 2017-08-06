import re
import html
import time
import json
import execjs

from .base import throttle
from .base import BaseCrawler
from .models import Raw, Kind

from bs4 import BeautifulSoup
import requests


class Crawler(BaseCrawler):
    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__(*args, **kwargs)
        self.site = 'tapotiexie'

    @throttle()
    def fetch_page(self, *args, **kwargs):
        r = super(Crawler, self).fetch_page(*args, **kwargs)
        if '亲爱的用户，请完成验证后继续访问' in r.text:
            # log.info('banned. sleep 100s')
            # time.sleep(100)
            # r = fetch_page(args, kwargs)
            raise ValueError('banned', r.url)
        return r

    def company_urls(self):
        root = 'http://www.tapotiexie.com'
        html = requests.get(url='http://www.tapotiexie.com/Ship/index.html')
        soup = BeautifulSoup(html.text, 'lxml')
        div_list = soup.find_all(class_='tptx_content1')
        url_list = []
        for i in div_list:
            url_list.append(i.a.get('href'))
        return [root + url for url in url_list]

    def company_page(self, url):
        r = self.fetch_page(url)
        raw = {'site': self.site,
               'url': url,
               'kind': Kind.COMPANY,
               'mime_type': 'text/html',
               'raw': r.text
               }
        Raw(raw).upsert()

    def ship_urls(self):
        root = 'http://www.tapotiexie.com'
        result = []
        for com_url in self.company_urls():
            html = requests.get(url=com_url)
            soup = BeautifulSoup(html.text, 'lxml')
            table_list = soup.find('table').find_all('a')
            for i in table_list:
                result.append(root + i.get('href'))
        return result

    def ship_page(self, url):
        r = self.fetch_page(url)
        raw = {'site': self.site,
               'url': url,
               'kind': Kind.SHIP,
               'mime_type': 'text/html',
               'raw': r.text
               }
        Raw(raw).upsert()

    def cruise_urls(self):
        root = 'http://www.tapotiexie.com'
        result = []
        for n in range(1, 26):
            html = requests.get(url='http://www.tapotiexie.com/Line/index/name/yt/port/'
                                    '0/mouth/0/company/0/p/{}.html'.format(n))
            soup = BeautifulSoup(html.text, 'lxml')
            for i in soup.find_all(class_='tptx_jcyj_2ac_2'):
                result.append(root + i.a.get('href'))
        return result

    def cruise_page(self, url):
        r = self.fetch_page(url)
        raw = {'site': self.site,
               'url': url,
               'kind': Kind.CRUISE,
               'mime_type': 'text/html',
               'raw': r.text
               }
        Raw(raw).upsert()

    def price_urls(self):
        result = self.cruise_urls()
        return result

    def price_page(self, url):
        r = self.fetch_page(url)
        raw = {'site': self.site,
               'url': url,
               'kind': Kind.PRICE,
               'mime_type': 'text/html',
               'raw': r.text
               }
        Raw(raw).upsert()
