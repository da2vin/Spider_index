# -*- coding: utf-8 -*-

import hashlib
import urllib
import json
import base64
import urllib2


def md5str(str):  # md5加密字符串
    m = hashlib.md5(str.encode(encoding="utf-8"))
    return m.hexdigest()


def md5(byte):  # md5加密byte
    return hashlib.md5(byte).hexdigest()


class DamatuApi():
    ID = '43311'
    KEY = 'd191c0fd4d6f1957067350f171409441'
    HOST = 'http://api.dama2.com:7766/app/'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getSign(self, param=b''):
        return (md5(bytearray(self.KEY, encoding="utf8") + bytearray(self.username, encoding="utf8") + param))[:8]

    def getPwd(self):
        return md5str(self.KEY + md5str(md5str(self.username) + md5str(self.password)))

    def post(self, path, params={}):
        data = urllib.urlencode(params).encode('utf-8')
        url = self.HOST + path
        req = urllib2.Request(url, data)
        return urllib2.urlopen(req).read()

    # 查询余额 return 是正数为余额 如果为负数 则为错误码
    def getBalance(self):
        data = {'appID': self.ID,
                'user': self.username,
                'pwd': dmt.getPwd(),
                'sign': dmt.getSign()
                }
        res = self.post('d2Balance', data)
        res = str(res, encoding="utf-8")
        jres = json.loads(res)
        if jres['ret'] == 0:
            return jres['balance']
        else:
            return jres['ret']

    # 上传验证码 参数filePath 验证码图片路径 如d:/1.jpg type是类型，查看http://wiki.dama2.com/index.php?n=ApiDoc.Pricedesc  return 是答案为成功 如果为负数 则为错误码
    def decode(self, fdata, type):
        filedata = base64.b64encode(fdata)
        data = {'appID': self.ID,
                'user': self.username,
                'pwd': dmt.getPwd(),
                'type': type,
                'fileDataBase64': filedata,
                'sign': dmt.getSign(fdata)
                }
        res = self.post('d2File', data)
        # res = str(res, encoding = "utf-8")
        jres = json.loads(res)
        if jres['ret'] == 0:
            # 注意这个json里面有ret，id，result，cookie，根据自己的需要获取
            return (jres['result'])
        else:
            return jres['ret']

    # url地址打码 参数 url地址  type是类型(类型查看http://wiki.dama2.com/index.php?n=ApiDoc.Pricedesc) return 是答案为成功 如果为负数 则为错误码
    def decodeUrl(self, url, type):
        data = {'appID': self.ID,
                'user': self.username,
                'pwd': dmt.getPwd(),
                'type': type,
                'url': urllib.parse.quote(url),
                'sign': dmt.getSign(url.encode(encoding="utf-8"))
                }
        res = self.post('d2Url', data)
        res = str(res, encoding="utf-8")
        jres = json.loads(res)
        if jres['ret'] == 0:
            # 注意这个json里面有ret，id，result，cookie，根据自己的需要获取
            return (jres['result'])
        else:
            return jres['ret']

    # 报错 参数id(string类型)由上传打码函数的结果获得 return 0为成功 其他见错误码
    def reportError(self, id):
        # f=open('0349.bmp','rb')
        # fdata=f.read()
        # print(md5(fdata))
        data = {'appID': self.ID,
                'user': self.username,
                'pwd': dmt.getPwd(),
                'id': id,
                'sign': dmt.getSign(id.encode(encoding="utf-8"))
                }
        res = self.post('d2ReportError', data)
        res = str(res, encoding="utf-8")
        jres = json.loads(res)
        return jres['ret']


# 调用类型实例：
# 1.实例化类型 参数是打码兔用户账号和密码
dmt = DamatuApi("iamDW", "maosu1989")
# #2.调用方法：
# print(dmt.getBalance()) #查询余额
# print(dmt.decode('0349.bmp',200)) #上传打码
# print(dmt.decodeUrl('http://captcha.qq.com/getimage?aid=549000912&r=0.7257105156128585&uin=3056517021',200)) #上传打码
# #print(dmt.reportError('894657096')) #上报错误
