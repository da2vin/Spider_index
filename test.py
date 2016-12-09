#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import csv
import time

reload(sys)
sys.setdefaultencoding('utf-8')

# with open('data.txt') as f:
#     line = f.readline()
#     jsonobj = json.loads(line)
#     key = ''
#     for obj in jsonobj:
#         key += "," + obj
#     print key

# with open('data.txt', 'r') as f:
#     line = f.readline()
#
#     while line:
#         jsonobj = json.loads(line).items()
#         csv_str = ''
#         for obj in jsonobj:
#             # if csv_str == '':
#             #     csv_str += obj[1]
#             # else:
#             csv_str += "," + obj[1]
#         print csv_str
#         with open('data.csv', 'a') as fs:
#             fs.write(csv_str + '\n')
#         line = f.readline()

# def check_pic(path):
#     with open(path, 'rb') as fs:
#         length = len(fs.read())
#         print length
#         if len(fs.read()) == 33:
#             return False
#         else:
#             return True

# print check_pic('pic_temp/element_1475034402.81.png')

# print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# print int(time.strftime('%Y%m%d', time.localtime(time.time())))

print '00100'.strip('0')