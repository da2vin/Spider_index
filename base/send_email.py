#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys
import setting
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def sendEmail(text):
    try:
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'指数爬虫 <%s>' % setting.EMAIL_ADDR)
        msg['To'] = _format_addr(u'DK <%s>' % setting.EMAIL_TO_ADDR)
        msg['Subject'] = Header(u'指数爬虫异常', 'utf-8').encode()

        server = smtplib.SMTP(setting.EMAIL_SMTP_SERVER, 25)
        server.set_debuglevel(1)
        server.login(setting.EMAIL_ADDR, setting.EMAIL_PASSWORD)
        server.sendmail(setting.EMAIL_ADDR, [setting.EMAIL_TO_ADDR], msg.as_string())
        server.quit()
    except:
        print '发送邮件失败：' + traceback.format_exc()

