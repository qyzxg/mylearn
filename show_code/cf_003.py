#!/usr/bin/python
# -*- coding:utf-8 -*-

from pymongo import *

from show_code.cf_001 import rcode

client = MongoClient('localhost', 27017)
db = client.test
collection = db.code

code_dict = {'%s' % i: rcode() for i in range(200)}
# collection.insert(code_dict)

# for i in range(200):
#     d = {'code':rcode()}
#     collection.insert(d)
from bson import ObjectId

print(collection.find_one({'_id': ObjectId('595e140207310024c425ff8e')}))
