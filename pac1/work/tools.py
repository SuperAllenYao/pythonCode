#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os.path
from  pac1 import con


def getFlieType(flie_name):
    """
    根据文件的后缀来判断文件的类型, flie name: str 文件名称, 返回的是文件类型 int
    -1: 未知文档
    0: 是图片类文件
    1: word文档
    2: excel文档
    3: PPT文档
    """
    #默认文件是未知类型
    result = con.FLIE_TYPE_UNKNOWN
    # if not os.path.isfile(flie_name):
    #     return = con.FLIE_TYPE_UNKNOWN
    path_name, ext = os.path.splitext(flie_name)
    #将文件后缀名同一转换为小写
    ext = ext.lower()
    # 图片类型的文件
    if ext in ('.png', '.jpg', '.gif', '.bmp'):
        result = con.FLIE_TYPE_IMG
    # word文档
    elif ext in ('.doc', 'docx'):
        result = con.FLIE_TYPE_DOC
    # excel文档
    elif ext in ('.xls', 'xlsx'):
        result = con.FLIE_TYPE_EXC
    # PPT文档
    elif ext in ('.ppt', '.pptx'):
        result = con.FLIE_TYPE_PPT
    return result
