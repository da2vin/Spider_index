#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback
import time
from selenium.webdriver.common.keys import Keys
import setting

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ali_index(web, keyword):
    result = None
    try:
        web.get('https://index.1688.com/alizs/keyword.htm')
        time.sleep(setting.SLEEP_TIME)

        item = dict()

        element = web.find_element_by_id('alizs-input')
        element.clear()
        element.send_keys(keyword.decode('utf-8'))
        element.send_keys(Keys.ENTER)
        time.sleep(setting.SLEEP_TIME)

        element = web.find_elements_by_css_selector('ul.page-list li a')[0]
        element.click()
        time.sleep(setting.SLEEP_TIME)

        # item['ali_1688buy_index'] = web.find_element_by_css_selector('p.right-detail span.highlight-red').get_attribute(
        #         'innerText').replace('第', '')

        element = web.find_element_by_css_selector('div[class=\'selected-list fd-clr list\']')
        item['ali_taobaobuy_index'] = element.find_element_by_css_selector('div.col-tb-purchase p').get_attribute(
                'innerText').replace(',', '')
        item['ali_1688buy_index'] = element.find_element_by_css_selector('div.col-1688-purchase p').get_attribute(
                'innerText').replace(',', '')
        item['ali_1688sup_index'] = element.find_element_by_css_selector('div.col-supply p').get_attribute(
                'innerText').replace(',', '')
        item['ali_taobao_needsfore'] = element.find_element_by_css_selector('p.col-forecast').get_attribute('innerText')

        element = web.find_elements_by_css_selector('ul.page-list li a')[2]
        element.click()
        time.sleep(setting.SLEEP_TIME)

        has_first_rect = '最近30天，在您所选行业老采购商人数过少，暂不提供新/老采购商身份分布' not in web.find_element_by_css_selector(
                'div.mod-identity').get_attribute('outerHTML')
        has_second_rect = '最近30天，在您所选行业淘宝店主采购商人数过少，暂不提供采购商的非淘宝/淘宝店主身份分布' not in web.find_element_by_css_selector(
                'div.mod-identity').get_attribute('outerHTML')
        has_third_rect = '最近30天，在您所选行业线上交易的供应商人数过少，暂不提供采购客单价分布。' not in web.find_element_by_css_selector(
                'div.mod-price').get_attribute('outerHTML')

        if has_first_rect and has_second_rect:
            elements = web.find_elements_by_css_selector('div[class=\'content detail\'] span.highlight-red')
            item['ali_newbuyer'] = elements[0].get_attribute('innerText')
            item['ali_buyer_puchaseQty'] = elements[1].get_attribute('innerText').replace('次以上', '')
            item['ali_buyer_taobao'] = elements[2].get_attribute('innerText')
            item['ali_buyer_taobao_grade'] = elements[3].get_attribute('innerText')
        elif has_first_rect and not has_second_rect:
            elements = web.find_elements_by_css_selector('div[class=\'content detail\'] span.highlight-red')
            item['ali_newbuyer'] = elements[0].get_attribute('innerText')
            item['ali_buyer_puchaseQty'] = elements[1].get_attribute('innerText').replace('次以上', '')
            item['ali_buyer_taobao'] = ''
            item['ali_buyer_taobao_grade'] = ''
        elif not has_first_rect and has_second_rect:
            elements = web.find_elements_by_css_selector('div[class=\'content detail\'] span.highlight-red')
            item['ali_newbuyer'] = ''
            item['ali_buyer_puchaseQty'] = ''
            item['ali_buyer_taobao'] = elements[0].get_attribute('innerText')
            item['ali_buyer_taobao_grade'] = elements[1].get_attribute('innerText')
        else:
            item['ali_newbuyer'] = ''
            item['ali_buyer_puchaseQty'] = ''
            item['ali_buyer_taobao'] = ''
            item['ali_buyer_taobao_grade'] = ''

        if has_third_rect:
            element = web.find_element_by_css_selector('div[class=\'obj-right obj-analyse\'] span.highlight-red')
            item['ali_buyer_unitprice'] = element.get_attribute('innerText')
        else:
            item['ali_buyer_unitprice'] = ''

        result = item
    except:
        print traceback.format_exc()
        # web.save_screenshot('pic_temp/screen_ali.png')
    finally:
        return result


def get_ali_source(ali_driver_pool, keyword):
    if not ali_driver_pool:
        return None
    web = ali_driver_pool.get()
    source = get_ali_index(web, keyword)
    ali_driver_pool.put(web)
    return source


def get_page_source(web):
    return web.execute_script("return document.documentElement.outerHTML")
