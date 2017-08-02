#!/usr/bin/python
# -*- coding:utf-8 -*-


from mysql.connector import connect

from show_code.cf_001 import rcode

conn = connect(host='localhost', user='root', passwd='qyzxg', db='test')
cusor = conn.cursor()
sql_create = '''CREATE TABLE IF NOT EXISTS code(id INT(4) PRIMARY KEY AUTO_INCREMENT, rcode VARCHAR(300))'''
cusor.execute(sql_create)

for i in range(200):
    s = rcode()
    print(s)
    sql_insert = "insert into code(rcode) values('%s')" % s
    cusor.execute(sql_insert)

conn.commit()
cusor.close()
conn.close()
