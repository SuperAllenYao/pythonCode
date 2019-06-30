#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ApiExcption(Exception):
    """ 我的自定义异常 """
    err_code = ''
    err_msg = ''

    def __init__(self, err_code=None, err_msg=None):
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return "Error: {} - {}".format(self.err_code, self.err_msg)


class InvalidCtrlExec(ApiExcption):
    """ 当参数不合法时触发 """
    err_code = '40001'
    err_msg = '不合法的调用凭证'

    def __init__(self, err_code=None, err_msg=None):
        self.err_code = err_code
        self.err_msg = err_msg


class BadPramsExcption(ApiExcption):
    """参数不正确"""
    err_code = '40002'
    err_msg = '参数必须为整数数字'


def divide(num1, num2):
    """ 除法的实现 """
    # 两个数必须为整数
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise BadPramsExcption()
    # 除数不能为零
    if num2 == 0:
        raise ApiExcption('40001', '除数不能为零')
    return num1 / num2


if __name__ == '__main__':
    try:
        rest = divide(5, 's')
        print(rest)
    except ApiExcption as err:
        print('出错了')
        print(err)
