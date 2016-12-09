#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from baidu_index.baidu_web_driver import baidu_web_driver_pool
from ali_index.ali_web_driver import ali_web_driver_pool
import setting
from multiprocessing.dummy import Pool as ThreadPool
import traceback
from baidu_index.baidu_web_driver.baidu_source import get_baidu_source
from ali_index.ali_web_driver.ali_source import get_ali_source
import json
from model.baidu.baidu_index_model import get_baidu_model, get_null_baidu_model
from model.ali.ali_index_model import get_ali_model, get_null_ali_model
import csv
from hbase.hbase_module import insert
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def init_pool():
    print '正在初始化百度指数爬取模块'
    '''
    生成百度指数搜索所用webkit池
    '''
    baidu_driver_pool = baidu_web_driver_pool.get_baidu_web_driver_pool(setting.DRIVER_POOL_SIZE,
                                                                        setting.BAIDU_USERNAME,
                                                                        setting.BAIDU_PASSWORD)
    print '正在初始化阿里指数爬取模块'
    '''
    生成阿里指数搜索所用webkit池
    '''
    ali_driver_pool = ali_web_driver_pool.get_ali_web_driver_pool(setting.DRIVER_POOL_SIZE)

    return baidu_driver_pool, ali_driver_pool


'''
读取所需爬取内容
'''
def keywords():
    reader = csv.reader(file('keywords_data.csv', 'rb'))
    for line in reader:
        yield line


'''
获取指数详情
'''
def get_index(baidu_driver_pool_temp, ali_driver_pool_temp, keyword_line):
    try:
        keyword = keyword_line[3].decode('gbk').strip()
        final_result = dict()
        for area_code in setting.AREA_LOCATION.iterkeys():

            print keyword + ';' + setting.AREA_REFLECTION[area_code] + '：百度指数开始搜索'

            need_search_top = setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_1' not in final_result.iterkeys()
            result_baidu = get_baidu_source(baidu_driver_pool_temp, keyword, area_code,
                                            need_search_top)  # 最后一个参数是为了不重复搜索区域排名
            if result_baidu is None:
                final_result = dict(final_result, **get_null_baidu_model(area_code, need_search_top))
            else:
                final_result = dict(final_result,
                                    **get_baidu_model(area_code, result_baidu, need_search_top))

            print keyword + ';' + setting.AREA_REFLECTION[area_code] + '：百度指数搜索完成'

        print keyword + '：阿里指数开始搜索'

        result_ali = get_ali_source(ali_driver_pool_temp, keyword)
        if result_ali is None:
            final_result = dict(final_result, **get_null_ali_model())
        else:
            final_result = dict(final_result, **get_ali_model(result_ali))

        print keyword + '：阿里指数搜索完成'

        final_result[setting.HBASE_INDEX_BASE_FAM + ':' + 'crawl_key'] = keyword
        final_result[setting.HBASE_INDEX_BASE_FAM + ':' + 'industry_name'] = keyword_line[2].decode('gbk')
        final_result[setting.HBASE_INDEX_BASE_FAM + ':' + 'industry_name_big'] = keyword_line[1].decode('gbk')

        datakey = keyword_line[0] + '_' + time.strftime('%Y%m', time.localtime(time.time()))
        timestamp = int(time.strftime('%Y%m%d', time.localtime(time.time())))
        insert(setting.HBASE_INDEX_TABLE_NAME, datakey, final_result, timestamp)

        # result = json.dumps(final_result, sort_keys=True, indent=4).decode('unicode-escape')
        result = json.dumps(final_result).decode('unicode-escape')
        print result

        return final_result
    except:
        print '-------------------------'
        print traceback.format_exc()
        print '--------------------------'


def main():
    try:
        baidu_driver_pool, ali_driver_pool = init_pool()
        thread_pool = ThreadPool(setting.DRIVER_POOL_SIZE)
        for keyword in keywords():
            thread_pool.apply_async(get_index, (baidu_driver_pool, ali_driver_pool, keyword))
        thread_pool.close()
        thread_pool.join()
    except:
        print traceback.format_exc()
    print '--------end--------'


if __name__ == '__main__':
    main()
