#!/usr/bin/python
# -*- coding:utf-8 -*-
from qiniu import Auth, put_data, PersistentFop, urlsafe_base64_encode
import time
import os

class UploadToQiniu():
    '''上传文件到七牛'''
    def __init__(self, file, prefix, domian_name='https://static.51qinqing.com', bucket_name='static', expire=3600, mark = False):
        self.access_key = os.environ.get('QINIU_ACCESS_KEY')
        self.secret_key = os.environ.get('QINIU_SECRET_KEY')
        self.bucket_name = bucket_name
        self.domian_name = domian_name
        self.file = file
        self.expire = expire
        self.prefix = prefix
        self.q = Auth(self.access_key, self.secret_key)
        self.pipeline = 'water_mark'
        self.fops = r'imageView2/0/q/75|watermark/2/text/d3d3LjUxcWlucWluZy5jb20=/font/6buR5L2T/fontsize/360/fill/I0ZGRkJGQg==/dissolve/100/gravity/SouthEast/dx/10/dy/10'
        self.mark = mark

    def water_mark(self, key):
        saveas_key = urlsafe_base64_encode('{}:{}'.format(self.bucket_name, key))
        fops = self.fops + '|saveas/' + saveas_key
        pfop = PersistentFop(self.q, self.bucket_name, self.pipeline)
        ops = list()
        ops.append(fops)
        pfop.execute(key, ops, 1)


    def upload(self):
        ext = self.file.name.split('.')[-1]
        time_ = str(time.time()).replace('.', '')
        k = self.prefix + time_ + '_' + '.' + ext
        token = self.q.upload_token(self.bucket_name, k, self.expire)
        a, b = put_data(token, k, self.file.read())
        if self.mark:
            self.water_mark(k)
        return a, b

    def upload_web(self, file_name, file):
        token = self.q.upload_token(self.bucket_name, file_name, self.expire)
        a, b = put_data(token, self.prefix + file_name, file)
        if self.mark:
            self.water_mark(self.prefix + file_name)
        return a, b


if __name__ == '__main__':
    file = open('1.png', 'rb')
    u = UploadToQiniu(file, 'test/', mark=True)
    a, b = u.upload()
    print(a['key'])
