#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import happybase
import setting
import json
import csv
import codecs

reload(sys)
sys.setdefaultencoding('utf-8')


def insert(table_name, key, data, timestamp):
    connection = happybase.Connection(setting.HBASE_HOST, port=setting.HBASE_PORT)
    table = connection.table(table_name)
    table.put(key, data, timestamp)
    connection.close()


def drop_table(table_name):
    connection = happybase.Connection(setting.HBASE_HOST, port=setting.HBASE_PORT)
    connection.disable_table(table_name)
    connection.delete_table(table_name)
    connection.close()


def create_table(table_name, table_families):
    connection = happybase.Connection(setting.HBASE_HOST, port=setting.HBASE_PORT)
    connection.create_table(table_name, families=table_families)
    connection.close()


def scan(table_name):
    connection = happybase.Connection(setting.HBASE_HOST, port=setting.HBASE_PORT)
    table = connection.table(table_name)
    items = table.scan()
    for item in items:
        print json.dumps(dict(item[1])).decode('unicode-escape')
    print(len(list(items)))
    connection.close()


def write_csv(table_name, file_name, key_filter='2016'):
    connection = happybase.Connection(setting.HBASE_HOST, port=setting.HBASE_PORT)
    table = connection.table(table_name)
    items = table.scan(filter="RowFilter(=,\'substring:%s\')" % (key_filter,))

    with open(file_name, 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8)
        spamwriter = csv.writer(csvfile, dialect='excel')
        i = 0
        for item in items:
            if i == 0:
                temp_dict = dict(item[1]).keys()
                temp_dict.append('key')
                spamwriter.writerow(temp_dict)
            temp_dict = dict(item[1]).values()
            temp_dict.append(item[0])
            spamwriter.writerow(temp_dict)
            i += 1

    connection.close()

# write_csv('index', 'data.csv', '201610')

# scan('index')

# drop_table('index')
# create_table('index', {'fam_exponent_info': dict(max_versions=31),
#                        'fam_baidu': dict(max_versions=31),
#                        'fam_ali': dict(max_versions=31),
#                        })
