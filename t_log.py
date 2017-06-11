#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import time
import random

# with open(r'E:\MyProject\deploy\access.log', 'r', encoding='utf-8') as file:
#     # file.seek(0,2)
#     # print(file.readlines(),file.tell())
#     # lst = []
#     # for l in file.readlines():
#     #     arr = l.split()
#     #     ip = arr[0]
#     #     time = datetime.datetime.strptime(arr[3][1:], '%d/%b/%Y:%H:%M:%S')
#     #     status = int(arr[8])
#     #     length = int(arr[9])
#     #     url = arr[10]
#     #     # brower = arr[11].split('/')[0].strip('"')
#     #     # system = arr[12].strip('(').strip(';')
#     #     req_time = float(arr[26])
#     #     res_time = float(arr[27])
#     #     lst.append(ip)
#     #     print(ip, time, status, length, url, req_time, res_time)
#     # pv = len(f)
#     # uv = len(set(lst))
#     # print(pv,uv)
#     for line in file.readlines():
#         for l in line.split():

# class ReadLog():
#     def __init__(self, logfile=r'E:\MyProject\deploy\access.log',
#                  seekfile=r'E:\MyProject\deploy\access.seek'):
#         self.logfile = logfile
#         self.seekfile = seekfile
#
#     def _write_seek(self, seek=0):  # 写入当前的seek位置
#         with open(self.seekfile, 'w+', encoding='utf-8') as file:
#             file.write(str(seek))
#
#     def _read_seek(self):  # 读取文件的seek位置
#         with open(self.seekfile, 'r', encoding='utf-8') as file:
#             result = file.read()
#             if result:
#                 return int(result)
#         return 0
#
#     def read_content(self):
#         file_seek = self._read_seek()
#         with open(self.logfile, 'r', encoding='utf-8') as file:
#             file.seek(file_seek, 0)
#             while True:
#                 _row = file.readline()
#                 file_seek += len(_row)
#                 self._write_seek(file_seek)
#                 print(_row)
#                 if not _row:
#                     break
#
#
#
# r = ReadLog()
# r.read_content()
#
# # with open(r'E:\MyProject\deploy\access.log', 'r', encoding='utf-8') as file:
# #     file.seek(345,0)
# #     f = file.readline()
# #     print(f)


#
# with open(r'E:\MyProject\deploy\access.log', 'r', encoding='utf-8') as file:
#         # file.write('112.13.54.213 - - [20/May/2017:07:02:40 +0000] 200 9589 "http://www.51datas.com/service" "-" 127.0.0.1:8080  0.228  {0:.3}'.format(random.random())+'\n')
#         # print('ok')
#         # time.sleep(5)
#     print(len(file.readlines()))

print(int(time.time()))