#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import setting

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ali_model_by_area(area_code, base_model):
    ali_model = dict()
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_1688buy_index'] = base_model['ali_1688buy_index']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_taobaobuy_index'] = base_model['ali_taobaobuy_index']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_1688sup_index'] = base_model['ali_1688sup_index']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_taobao_needsfore'] = base_model['ali_taobao_needsfore']

    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_newbuyer'] = base_model['ali_newbuyer']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_puchaseQty'] = base_model['ali_buyer_puchaseQty']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_taobao'] = base_model['ali_buyer_taobao']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_taobao_grade'] = base_model['ali_buyer_taobao_grade']
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_unitprice'] = base_model['ali_buyer_unitprice']
    return ali_model

def get_ali_model(base_model):
    ali_model = dict()
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_1688buy_index'] = base_model['ali_1688buy_index']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_taobaobuy_index'] = base_model['ali_taobaobuy_index']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_1688sup_index'] = base_model['ali_1688sup_index']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_taobao_needsfore'] = base_model['ali_taobao_needsfore']

    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_newbuyer'] = base_model['ali_newbuyer']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_puchaseQty'] = base_model['ali_buyer_puchaseQty']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_taobao'] = base_model['ali_buyer_taobao']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_taobao_grade'] = base_model['ali_buyer_taobao_grade']
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_unitprice'] = base_model['ali_buyer_unitprice']
    return ali_model

def get_null_ali_model_by_area(area_code):
    ali_model = dict()
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_1688buy_index'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_taobaobuy_index'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_1688sup_index'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_taobao_needsfore'] = ''

    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_newbuyer'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_puchaseQty'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_taobao'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_taobao_grade'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + area_code + '_' + 'ali_buyer_unitprice'] = ''
    return ali_model

def get_null_ali_model():
    ali_model = dict()
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_1688buy_index'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_taobaobuy_index'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_1688sup_index'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_taobao_needsfore'] = ''

    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_newbuyer'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_puchaseQty'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_taobao'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_taobao_grade'] = ''
    ali_model[setting.HBASE_ALI_FAM + ':' + 'ali_buyer_unitprice'] = ''
    return ali_model
