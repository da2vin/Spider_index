#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import threading

mutex = threading.Lock()


def get_vcode(path):
    with Image.open(path) as image:
        mutex.acquire(1)
        vcode = pytesseract.image_to_string(image, lang='numfont')
        mutex.release()
        return vcode.replace(',', '').replace('\n', '')


def get_vcode_by_img_0(img):
    mutex.acquire(1)
    vcode = pytesseract.image_to_string(img, lang='numfont')
    if vcode == '':
        img = merge_thumb_0(img)
        vcode = pytesseract.image_to_string(img, lang='numfont')
        if vcode == '00':
            vcode = '0'
        else:
            vcode = vcode.strip('0')
    mutex.release()
    return vcode.replace(',', '').replace('\n', '')


def get_vcode_by_img_1(img):
    mutex.acquire(1)
    vcode = pytesseract.image_to_string(img, lang='numfont')
    if vcode == '':
        img = merge_thumb_1(img)
        vcode = pytesseract.image_to_string(img, lang='numfont')
        if vcode == '00':
            vcode = '0'
        else:
            vcode = vcode.strip('0')
    mutex.release()
    return vcode.replace(',', '').replace('\n', '')

'''
个位数图片无法识别，另外融合一个图片来识别，此为黑底图片
'''
def merge_thumb_0(image_need_merge):
    image_0 = Image.open('tesseract_ocr/0_0.png')
    size_need_merge = image_need_merge.size
    size_0 = image_0.size

    merge_image = Image.new('RGBA', (size_need_merge[0] + size_0[0], size_need_merge[1]))
    merge_image.paste(image_0, (0, 0))
    merge_image.paste(image_need_merge, (size_0[0], 0))

    # merge_image.save('pic_temp/merged.png')
    return merge_image

'''
个位数图片无法识别，另外融合一个图片来识别，此为白底图片
'''
def merge_thumb_1(image_need_merge):
    image_0 = Image.open('tesseract_ocr/0_1.png')
    size_need_merge = image_need_merge.size
    size_0 = image_0.size

    merge_image = Image.new('RGBA', (size_need_merge[0] + size_0[0], size_need_merge[1]))
    merge_image.paste(image_need_merge, (0, 0))
    merge_image.paste(image_0, (size_need_merge[0], 0))

    # merge_image.save('pic_temp/merged.png')
    return merge_image

# import cv
# def white_and_black(pic_name):
#     image = cv.LoadImage(pic_name, 0)
#     size = (image.width, image.height)
#     iTmp = cv.CreateImage(size, image.depth, image.nChannels)
#     for i in range(image.height):
#         for j in range(image.width):
#             if image[i, j] < 100:
#                 iTmp[i, j] = 255
#             else:
#                 iTmp[i, j] = 0
#
#     cv.SaveImage(pic_name, iTmp)

# get_vcode('merged.png')
# merge_thumb('111.png')
