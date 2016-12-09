#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from PIL import Image
from dama.damatu.damatuWeb import dmt
import setting
from selenium.webdriver.common.keys import Keys

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.resourceTimeout"] = 10
dcap["phantomjs.page.settings.loadImages"] = True
dcap["phantomjs.page.settings.userAgent"] = (setting.USER_AGENT)


def login_baidu(username, password):
    if setting.PHANTOMJS_SERVICE:
        web = webdriver.PhantomJS(service_args=setting.PHANTOMJS_SERVICE, executable_path=setting.PHANTOMJS_PATH,
                                  desired_capabilities=dcap)
    else:
        web = webdriver.PhantomJS(executable_path=setting.PHANTOMJS_PATH, desired_capabilities=dcap)

    web.get('https://passport.baidu.com/v2/?login')

    cookies = []

    element = web.find_element_by_id('TANGRAM__PSP_3__userName')
    element.clear()
    element.send_keys(username)

    element = web.find_element_by_id('TANGRAM__PSP_3__password')
    element.clear()
    element.send_keys(password)

    element = web.find_element_by_id('TANGRAM__PSP_3__submit')
    element.click()
    time.sleep(3)

    while True:
        if '帐号设置' in web.find_element_by_css_selector('title').get_attribute('innerText'):
            print '登录成功'
            cookies = web.get_cookies()
            break
        errorMsg = web.find_element_by_id('TANGRAM__PSP_3__error').get_attribute('innerText')
        if errorMsg == '请输入验证码':
            print errorMsg
            authcode = _get_authcode(web)
            element = web.find_element_by_id('TANGRAM__PSP_3__verifyCode')
            element.clear()
            element.send_keys(authcode)

            element = web.find_element_by_id('TANGRAM__PSP_3__submit')
            element.click()
            time.sleep(3)
        elif errorMsg == '您输入的验证码有误':
            print errorMsg
            element = web.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg')
            element.click()
            time.sleep(1)
            authcode = _get_authcode(web)
            element = web.find_element_by_id('TANGRAM__PSP_3__verifyCode')
            element.clear()
            element.send_keys(authcode)
            element.send_keys(Keys.ENTER)

            # element = web.find_element_by_id('TANGRAM__PSP_3__submit')
            # element.click()
            time.sleep(3)
            # web.save_screenshot('screen_baidu.png')
        else:
            print errorMsg
            cookies = None
            break

    web.close()
    return cookies


def _get_authcode(web):
    web.save_screenshot('authcode_baidu.png')
    element = web.find_element_by_id('TANGRAM__PSP_3__verifyCodeImgParent')

    left = 800
    top = 352
    right = left + element.size['width']
    bottom = top + element.size['height']

    im = Image.open('authcode_baidu.png')
    im = im.crop((left, top, right, bottom))
    im.save('authcode_baidu.png')

    data = _get_bytes('authcode_baidu.png')
    result = dmt.decode(data, 71)
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
