#!/usr/bin/python
# -*- coding:utf-8 -*-

from mysql.connector import connect
import re
import datetime
import time

conn = connect(host='localhost', user='qyzxg', password='qyzxg', database='test')
cur = conn.cursor()

# cur.execute('SELECT count(id) from 2000W')
# print(cur.fetchall())

area_dict = {11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古",
             21: "辽宁", 22: "吉林", 23: "黑龙江",
             31: "上海", 32: "江苏", 33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东",
             41: "河南", 42: "湖北", 43: "湖南", 44: "广东", 45: "广西", 46: "海南",
             50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏",
             61: "陕西", 62: "甘肃", 63: "青海", 64: "宁夏", 65: "新疆", 66: "新疆兵团",
             71: "台湾", 81: "香港", 82: "澳门", 91: "外国"}
id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']


def check_idcard(id_number):
    if not id_number:
        return False
    id_number = id_number.strip()
    try:
        if len(id_number) != 18:
            return False
    except:
        return False
    if not re.match(r'^\d{17}(\d|X|x)$', id_number):
        return False
    if int(id_number[0:2]) not in area_dict:
        return False
    try:
        datetime.date(int(id_number[6:10]), int(id_number[10:12]), int(id_number[12:14]))
    except:
        return False
    if check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in id_number[:-1]])]) % 11] != \
            id_number.upper()[-1]:
        return False
    return True


cur.execute('SELECT id,CtfId FROM 2000W')
for card in cur.fetchall():
    y = card[1].strip()[6:10]
    m = card[1].strip()[10:12]
    d = card[1].strip()[12:14]
    # dat = time.strptime('{}{}{}'.format(y, m, d), '%Y%m%d')
    print('{}-{}-{}'.format(y, m, d), card[1])
    cur.execute('update 2000W set Birthday="{}-{}-{}" WHERE id={}'.format(y,m,d, card[0]))
cur.close()
conn.commit()
conn.close()
