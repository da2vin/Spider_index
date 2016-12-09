#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue
import sys
import baidu_login_module
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import setting
import pickle
import os

reload(sys)
sys.setdefaultencoding('utf-8')

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.resourceTimeout"] = 10
dcap["phantomjs.page.settings.loadImages"] = True
dcap["phantomjs.page.settings.userAgent"] = (setting.USER_AGENT)


def _get_base_baidu_driver(cookies):
    if setting.PHANTOMJS_SERVICE:
        web = webdriver.PhantomJS(service_args=setting.PHANTOMJS_SERVICE, executable_path=setting.PHANTOMJS_PATH
                                  , desired_capabilities=dcap)
    else:
        web = webdriver.PhantomJS(executable_path=setting.PHANTOMJS_PATH
                                  , desired_capabilities=dcap)
    for cookie in cookies:
        web.add_cookie(cookie)

    return web

'''
获取一个webkit池，若cookie已经保存，则使用已保存cookie，若没有则执行登录
'''
def get_baidu_web_driver_pool(num, username, password):
    cookies = get_cookie()
    if not cookies:
        cookies = baidu_login_module.login_baidu(username, password)
        save_cookie(cookies)
    driver_queue = Queue.Queue()
    if not cookies:
        return None
    else:
        i = 0
        while i < num:
            web = _get_base_baidu_driver(cookies)
            driver_queue.put(web)
            i += 1
    return driver_queue


def save_cookie(cookies):
    with open('cookies.pkl', 'wb') as output:
        pickle.dump(cookies, output)


def get_cookie():
    if os.path.exists('cookies.pkl'):
        with open('cookies.pkl', 'rb') as cookie_file:
            cookies = pickle.load(cookie_file)
        return cookies
    else:
        return None
