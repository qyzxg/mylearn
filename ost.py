#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

a = os.environ.get('MAIL_PASSWORD')
for (dir_path,dir_names,filenames) in os.walk(os.getcwd(),topdown=True):
    for file in filenames:
        print(os.path.join(dir_path,file))
