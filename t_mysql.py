#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String,Integer ,Column,create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector


engine = create_engine('mysql+mysqlconnector://root:qyzxg@localhost:3306/hello',echo=True)
Base = declarative_base()
DBsession = sessionmaker(bind=engine)

a = os.getenv('MAIL_DEFAULT_SENDER')
print(a)

conn = mysql.connector.connect(user='myblog',
                               database='blog',
                               password='qyzxg',
                               host='13.112.193.37',
                               port='3306')

cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
values = cursor.fetchall()
print(values)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False,unique=True)
    age = Column(Integer,nullable=False)
    password = Column(String(64),nullable=False)
    email = Column(String(32),unique=True)

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),nullable=False,unique=True)
    content = Column(String(64),nullable=False)
    user_id = Column(Integer)

# Base.metadata.create_all(engine)
# session = DBsession()
# blogs = [Blog(title='的撒多所多',content='wgwrgwgwrgrw',user_id=1),
#          Blog(title='供热个人三个人', content='534特非', user_id=1),
#          Blog(title='果然是给我个', content='广东分公司答复', user_id=3)]
# session.add_all(blogs)
# session.commit()
# session.close()


session = DBsession()
query = session.query(User.name, Blog.title).join(Blog, User.id==Blog.user_id).filter(User.age==27)
for user,title in query:
    print(user,title)
