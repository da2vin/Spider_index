#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import setting

reload(sys)
sys.setdefaultencoding('utf-8')


def get_baidu_model(area_code, base_model, need_top):
    baidu_model = dict()
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_overa_index'] = base_model['baidu_overa_index']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_mbl_index'] = base_model['baidu_mbl_index']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_overa_yearbase'] = base_model['baidu_overa_yearbase']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_overa_chain'] = base_model['baidu_overa_chain']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_mbl_yearbase'] = base_model['baidu_mbl_yearbase']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_mbl_chain'] = base_model['baidu_mbl_chain']

    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_7'] = base_model['baidu_avg_7']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_30'] = base_model['baidu_avg_30']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_90'] = base_model['baidu_avg_90']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_180'] = base_model['baidu_avg_180']
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_all'] = base_model['baidu_avg_all']

    if need_top:
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_1'] = base_model['baidu_prov_1']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_2'] = base_model['baidu_prov_2']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_3'] = base_model['baidu_prov_3']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_4'] = base_model['baidu_prov_4']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_5'] = base_model['baidu_prov_5']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_6'] = base_model['baidu_prov_6']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_7'] = base_model['baidu_prov_7']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_8'] = base_model['baidu_prov_8']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_9'] = base_model['baidu_prov_9']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_10'] = base_model['baidu_prov_10']

        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_1'] = base_model['baidu_area_1']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_2'] = base_model['baidu_area_2']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_3'] = base_model['baidu_area_3']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_4'] = base_model['baidu_area_4']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_5'] = base_model['baidu_area_5']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_6'] = base_model['baidu_area_6']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_7'] = base_model['baidu_area_7']

        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_1'] = base_model['baidu_city_1']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_2'] = base_model['baidu_city_2']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_3'] = base_model['baidu_city_3']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_4'] = base_model['baidu_city_4']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_5'] = base_model['baidu_city_5']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_6'] = base_model['baidu_city_6']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_7'] = base_model['baidu_city_7']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_8'] = base_model['baidu_city_8']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_9'] = base_model['baidu_city_9']
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_10'] = base_model['baidu_city_10']
    return baidu_model

def get_null_baidu_model(area_code, need_top):
    baidu_model = dict()
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_overa_index'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_mbl_index'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_overa_yearbase'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_overa_chain'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_mbl_yearbase'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_mbl_chain'] = ''

    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_7'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_30'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_90'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_180'] = ''
    baidu_model[setting.HBASE_BAIDU_FAM + ':' + area_code + '_' + 'baidu_avg_all'] = ''

    if need_top:
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_1'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_2'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_3'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_4'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_5'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_6'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_7'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_8'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_9'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_prov_10'] = ''

        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_1'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_2'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_3'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_4'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_5'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_6'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_area_7'] = ''

        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_1'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_2'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_3'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_4'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_5'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_6'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_7'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_8'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_9'] = ''
        baidu_model[setting.HBASE_BAIDU_FAM + ':' + 'baidu_city_10'] = ''
    return baidu_model
