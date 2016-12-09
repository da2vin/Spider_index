#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# PHANTOMJS_PATH = '/root/phantomjs/phantomjs'
PHANTOMJS_PATH = 'C:/Python27/phantomjs.exe'
# PHANTOMJS_SERVICE = [
#     '--proxy=localhost:8888',
#     '--proxy-type=http',
#     # '--proxy-auth=username:password'
# ]
PHANTOMJS_SERVICE = None
DRIVER_POOL_SIZE = 1

BAIDU_USERNAME = '13408415919'
BAIDU_PASSWORD = 'dElete2404'

HBASE_HOST = '192.168.2.240'
HBASE_PORT = 9090

REFLECTION = {
    '<i style=\"background-position:-0px -2px;\"></i>': '0',
    '<i style=\"background-position:-8px -2px;\"></i>': '1',
    '<i style=\"background-position:-16px -2px;\"></i>': '2',
    '<i style=\"background-position:-24px -2px;\"></i>': '3',
    '<i style=\"background-position:-32px -2px;\"></i>': '4',
    '<i style=\"background-position:-40px -2px;\"></i>': '5',
    '<i style=\"background-position:-48px -2px;\"></i>': '6',
    '<i style=\"background-position:-56px -2px;\"></i>': '7',
    '<i style=\"background-position:-64px -2px;\"></i>': '8',
    '<i style=\"background-position:-72px -2px;\"></i>': '9',
    '<i style=\"background-position:-80px -2px;\"></i>': '%',
}

HBASE_BAIDU_FAM = 'fam_baidu'
HBASE_ALI_FAM = 'fam_ali'
HBASE_INDEX_BASE_FAM = 'fam_exponent_info'
HBASE_INDEX_TABLE_NAME = 'index'

AREA_REFLECTION = {
    'sc_cd': '四川_成都',
    'sc_my': '四川_绵阳',
    'gd_gz': '广东_广州',
    'qg_qg': '全国_全国',
}

AREA_LOCATION = {
    # 'sc_cd': '四川_成都',
    # 'sc_my': '四川_绵阳',
    # 'gd_gz': '广东_广州',
    'qg_qg': '全国_全国',
}

SLEEP_TIME = 1

EMAIL_ADDR = 'darkwings_love@163.com'
EMAIL_PASSWORD = 'bekilledmjw1989'
EMAIL_SMTP_SERVER = 'smtp.163.com'
EMAIL_TO_ADDR = '642811191@qq.com'

BAIDU_AVG_SLEEP_TIME = 2
