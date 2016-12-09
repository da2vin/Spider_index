#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from selenium.webdriver.common.keys import Keys
import time
import traceback
import setting
from dama.damatu.damatuWeb import dmt
from PIL import Image
from tesseract_ocr.tesseract_ocr_module import get_vcode_by_img_0, get_vcode_by_img_1
import os
from selenium.webdriver.common.action_chains import ActionChains
import copy
from base.send_email import sendEmail

reload(sys)
sys.setdefaultencoding('utf-8')


def get_baidu_index(web, keyword, area_code, need_search_top_area):
    result = None
    try:
        web.get('http://index.baidu.com')
        # web.save_screenshot('pic_temp/screen_baidu.png')
        element = web.find_element_by_id('schword')
        element.clear()
        element.send_keys(keyword.decode('utf-8'))
        element.send_keys(Keys.ENTER)
        time.sleep(setting.SLEEP_TIME * 3)

        while '请输入验证码' in get_page_source(web):
            print '需要验证码,保存截图并结束搜索'
            web.save_screenshot('pic_temp/need_authcode_%s.png' % (str(time.time()),))
            sendEmail('%s;-1' % (keyword,))
            os._exit(0)
            return result

            # region 暂时注释掉打码
            '''
            element = web.find_element_by_css_selector('input.verifyInput')
            element.clear()

            authcode = _get_authcode(web)
            if 'ERROR' in authcode:
                continue

            element.send_keys(authcode)

            element = web.find_element_by_css_selector('a.tang-dialog-button')
            element.click()

            time.sleep(setting.SLEEP_TIME)
            '''
            # endregion
        if '未被收录，如要查看相关数据，您需要购买创建新词的权限' in get_page_source(web):
            print '关键字：' + keyword + '未被百度收录'
            return result

        # region 选择地区
        if area_code != 'qg_qg':
            area = setting.AREA_REFLECTION[area_code].split('_')
            element = web.find_element_by_css_selector('div#compOtharea div.comCtl span.holdBox')
            element.click()
            time.sleep(setting.SLEEP_TIME * 0.6)

            element = web.find_elements_by_css_selector('div#compOtharea div.sltOpt')[0].find_element_by_xpath(
                    '//a[contains(.,\'%s\')]' % (area[0],))
            element.click()
            time.sleep(setting.SLEEP_TIME * 0.6)

            element = web.find_elements_by_css_selector('div#compOtharea div.sltOpt')[1].find_element_by_xpath(
                    '//a[contains(.,\'%s\')]' % (area[1],))
            element.click()
            time.sleep(setting.SLEEP_TIME * 0.6)

        # web.save_screenshot('pic_temp/screen_baidu.png')
        # endregion

        element = web.find_element_by_css_selector('a.gColor1')
        element.click()
        time.sleep(setting.SLEEP_TIME)
        time.sleep(setting.SLEEP_TIME)
        item = dict()

        elements = web.find_elements_by_css_selector('span.ftlwhf')

        item['baidu_overa_index'] = _get_value_by_ocr(web, elements[6])
        item['baidu_mbl_index'] = _get_value_by_ocr(web, elements[7])

        item['baidu_overa_yearbase'] = get_value(elements[8])
        item['baidu_overa_chain'] = get_value(elements[9])

        item['baidu_mbl_yearbase'] = get_value(elements[10])
        item['baidu_mbl_chain'] = get_value(elements[11])

        element = web.find_element_by_css_selector('label#trend-meanline')
        element.click()
        time.sleep(setting.SLEEP_TIME)

        # region avg_7 ---------------------------------
        element = web.find_element_by_css_selector('a[rel=\'7\']')
        element.click()
        time.sleep(setting.SLEEP_TIME)

        element = web.find_elements_by_css_selector('rect[x=\'45\']')[0]
        element.click()
        time.sleep(setting.BAIDU_AVG_SLEEP_TIME)

        element = web.find_element_by_css_selector('div.contentWord')
        location = copy.copy(element.location)
        size = copy.copy(element.size)
        pic_name = 'pic_temp/element_%s.png' % (str(time.time()),)
        web.save_screenshot(pic_name)

        left = location['x'] + 2
        top = location['y'] + 2
        right = left + size['width'] - 4
        bottom = top + size['height'] - 4

        with Image.open(pic_name) as im:
            im = im.crop((left, top, right, bottom))
            im.save(pic_name)
            item['baidu_avg_7'] = get_vcode_by_img_0(im)
        if os.path.exists(pic_name) and item['baidu_avg_7'] != '':
            os.remove(pic_name)
        # endregion ---------------------------------

        # region avg_30 ---------------------------------
        element = web.find_element_by_css_selector('a[rel=\'30\']')
        element.click()
        time.sleep(setting.SLEEP_TIME)

        ActionChains(web).move_to_element(element).perform()
        time.sleep(setting.SLEEP_TIME)

        element = web.find_elements_by_css_selector('rect[x=\'45\']')[0]
        element.click()
        time.sleep(setting.BAIDU_AVG_SLEEP_TIME)

        element = web.find_element_by_css_selector('div.contentWord')
        location = copy.copy(element.location)
        size = copy.copy(element.size)
        pic_name = 'pic_temp/element_%s.png' % (str(time.time()),)
        web.save_screenshot(pic_name)

        left = location['x'] + 2
        top = location['y'] + 2
        right = left + size['width'] - 4
        bottom = top + size['height'] - 4

        with Image.open(pic_name) as im:
            im = im.crop((left, top, right, bottom))
            im.save(pic_name)
            item['baidu_avg_30'] = get_vcode_by_img_0(im)
        if os.path.exists(pic_name) and item['baidu_avg_30'] != '':
            os.remove(pic_name)
        # endregion ---------------------------------

        # region avg_90 ---------------------------------
        element = web.find_element_by_css_selector('a[rel=\'90\']')
        element.click()
        time.sleep(setting.SLEEP_TIME)

        ActionChains(web).move_to_element(element).perform()
        time.sleep(setting.SLEEP_TIME)

        element = web.find_elements_by_css_selector('rect[x=\'45\']')[0]
        element.click()
        time.sleep(setting.BAIDU_AVG_SLEEP_TIME)

        element = web.find_element_by_css_selector('div.contentWord')
        location = copy.copy(element.location)
        size = copy.copy(element.size)
        pic_name = 'pic_temp/element_%s.png' % (str(time.time()),)
        web.save_screenshot(pic_name)

        left = location['x'] + 2
        top = location['y'] + 2
        right = left + size['width'] - 4
        bottom = top + size['height'] - 4

        with Image.open(pic_name) as im:
            im = im.crop((left, top, right, bottom))
            im.save(pic_name)
            item['baidu_avg_90'] = get_vcode_by_img_0(im)
        if os.path.exists(pic_name) and item['baidu_avg_90'] != '':
            os.remove(pic_name)
        # endregion ---------------------------------

        # region avg_180 ---------------------------------
        element = web.find_element_by_css_selector('a[rel=\'180\']')
        element.click()
        time.sleep(setting.SLEEP_TIME)

        ActionChains(web).move_to_element(element).perform()
        time.sleep(setting.SLEEP_TIME)

        element = web.find_elements_by_css_selector('rect[x=\'45\']')[0]
        element.click()
        time.sleep(setting.BAIDU_AVG_SLEEP_TIME)

        element = web.find_element_by_css_selector('div.contentWord')
        location = copy.copy(element.location)
        size = copy.copy(element.size)
        pic_name = 'pic_temp/element_%s.png' % (str(time.time()),)
        web.save_screenshot(pic_name)

        left = location['x'] + 2
        top = location['y'] + 2
        right = left + size['width'] - 4
        bottom = top + size['height'] - 4

        with Image.open(pic_name) as im:
            im = im.crop((left, top, right, bottom))
            im.save(pic_name)
            item['baidu_avg_180'] = get_vcode_by_img_0(im)
        if os.path.exists(pic_name) and item['baidu_avg_180'] != '':
            os.remove(pic_name)
        # endregion ---------------------------------

        # region avg_all ---------------------------------
        element = web.find_element_by_css_selector('a[rel=\'all\']')
        element.click()
        time.sleep(setting.SLEEP_TIME)

        ActionChains(web).move_to_element(element).perform()
        time.sleep(setting.SLEEP_TIME)

        element = web.find_elements_by_css_selector('rect[x=\'45\']')[0]
        element.click()
        time.sleep(setting.BAIDU_AVG_SLEEP_TIME)

        element = web.find_element_by_css_selector('div.contentWord')
        location = copy.copy(element.location)
        size = copy.copy(element.size)
        pic_name = 'pic_temp/element_%s.png' % (str(time.time()),)
        web.save_screenshot(pic_name)

        left = location['x'] + 2
        top = location['y'] + 2
        right = left + size['width'] - 4
        bottom = top + size['height'] - 4

        with Image.open(pic_name) as im:
            im = im.crop((left, top, right, bottom))
            im.save(pic_name)
            item['baidu_avg_all'] = get_vcode_by_img_0(im)
        if os.path.exists(pic_name) and item['baidu_avg_all'] != '':
            os.remove(pic_name)
        # endregion ---------------------------------

        if need_search_top_area:
            element = web.find_elements_by_css_selector('table#subNav td')[3].find_element_by_css_selector('a')
            element.click()
            time.sleep(setting.SLEEP_TIME * 3.5)

            element = web.find_element_by_css_selector('div.grpArea svg text[text-anchor=\'middle\']')
            if 'display: none;' not in element.get_attribute('style'):
                item['baidu_prov_1'] = ''
                item['baidu_prov_2'] = ''
                item['baidu_prov_3'] = ''
                item['baidu_prov_4'] = ''
                item['baidu_prov_5'] = ''
                item['baidu_prov_6'] = ''
                item['baidu_prov_7'] = ''
                item['baidu_prov_8'] = ''
                item['baidu_prov_9'] = ''
                item['baidu_prov_10'] = ''

                item['baidu_area_1'] = ''
                item['baidu_area_2'] = ''
                item['baidu_area_3'] = ''
                item['baidu_area_4'] = ''
                item['baidu_area_5'] = ''
                item['baidu_area_6'] = ''
                item['baidu_area_7'] = ''

                item['baidu_city_1'] = ''
                item['baidu_city_2'] = ''
                item['baidu_city_3'] = ''
                item['baidu_city_4'] = ''
                item['baidu_city_5'] = ''
                item['baidu_city_6'] = ''
                item['baidu_city_7'] = ''
                item['baidu_city_8'] = ''
                item['baidu_city_9'] = ''
                item['baidu_city_10'] = ''
            else:
                elements = web.find_elements_by_css_selector('div.items')
                item['baidu_prov_1'] = elements[0].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_2'] = elements[1].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_3'] = elements[2].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_4'] = elements[3].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_5'] = elements[4].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_6'] = elements[5].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_7'] = elements[6].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_8'] = elements[7].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_9'] = elements[8].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_prov_10'] = elements[9].find_element_by_css_selector('td.scName').get_attribute('innerText')

                element = web.find_elements_by_css_selector('ul.scTab li')[1]
                element.click()
                time.sleep(setting.SLEEP_TIME)
                elements = web.find_elements_by_css_selector('div.items')
                item['baidu_area_1'] = elements[0].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_area_2'] = elements[1].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_area_3'] = elements[2].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_area_4'] = elements[3].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_area_5'] = elements[4].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_area_6'] = elements[5].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_area_7'] = elements[6].find_element_by_css_selector('td.scName').get_attribute('innerText')

                element = web.find_elements_by_css_selector('ul.scTab li')[2]
                element.click()
                time.sleep(setting.SLEEP_TIME)
                elements = web.find_elements_by_css_selector('div.items')
                item['baidu_city_1'] = elements[0].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_2'] = elements[1].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_3'] = elements[2].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_4'] = elements[3].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_5'] = elements[4].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_6'] = elements[5].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_7'] = elements[6].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_8'] = elements[7].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_9'] = elements[8].find_element_by_css_selector('td.scName').get_attribute('innerText')
                item['baidu_city_10'] = elements[9].find_element_by_css_selector('td.scName').get_attribute('innerText')

        result = item
    except:
        if '请输入验证码' in get_page_source(web):
            print '需要验证码,保存截图并结束搜索'
            web.save_screenshot('pic_temp/need_authcode_%s.png' % (str(time.time()),))
            sendEmail('%s;-1' % (keyword,))
            os._exit(0)

        print '---------------'
        print traceback.format_exc()
        print '---------------'
        error_pic_name = 'pic_temp/error_%s.png' % (str(time.time()),)
        web.save_screenshot(error_pic_name)
        sendEmail('关键字：%s\r\n%s\r\n%s' % (keyword, traceback.format_exc(), error_pic_name))
    finally:
        return result


def get_value(span):
    str_value = span.get_attribute('innerText')

    i_s = span.find_elements_by_css_selector('i')
    for i in i_s:
        str_value += setting.REFLECTION[i.get_attribute('outerHTML')]
    return str_value


def get_baidu_source(baidu_driver_pool, keyword, area_code, need_search_top_area):
    if not baidu_driver_pool:
        return None
    web = baidu_driver_pool.get()
    source = get_baidu_index(web, keyword, area_code, need_search_top_area)
    baidu_driver_pool.put(web)
    return source


def get_page_source(web):
    return web.execute_script("return document.documentElement.outerHTML")


def _get_value_by_ocr(web, element):
    # print element.get_attribute('outerHTML')
    pic_name = 'pic_temp/element_%s.png' % (str(time.time()),)
    web.save_screenshot(pic_name)

    left = element.location['x']
    top = element.location['y']
    right = left + element.size['width']
    bottom = top + element.size['height']

    with Image.open(pic_name) as im:
        im = im.crop((left, top, right, bottom))
        im.save(pic_name)
        vcode = get_vcode_by_img_1(im)
    if os.path.exists(pic_name):
        os.remove(pic_name)
    return vcode


def _get_authcode(web):
    print '指数页面打码1次'
    web.save_screenshot('pic_temp/authcode_baidu_index.png')
    element = web.find_element_by_css_selector('img.verifyImg')

    left = element.location['x']
    top = element.location['y']
    right = left + element.size['width']
    bottom = top + element.size['height']

    with Image.open('pic_temp/authcode_baidu_index.png') as im:
        im = im.crop((left, top, right, bottom))
        im.save('pic_temp/authcode_baidu_index.png')

        data = _get_bytes('pic_temp/authcode_baidu_index.png')
        result = dmt.decode(data, 42)
        print ' 指数页面打码结果：' + result
    return result


def _get_bytes(path):
    list_data = []
    f = open(path, 'rb')
    f.seek(0, 0)
    while True:
        t_byte = f.read(1)
        if len(t_byte) == 0:
            break
        else:
            list_data.append(ord(t_byte))
    list_data = bytearray(list_data)
    return list_data
