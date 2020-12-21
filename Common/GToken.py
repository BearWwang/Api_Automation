# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： GToken.py
# 开发工具 ： PyCharm
_global_dict = {}

def _init():
    global _global_dict
    _global_dict = {}

def set_value(key, value):
    """ 定义一个全局变量 """
    # print('==================================================================')
    # print('write....', key, value)
    _global_dict[key] = value
    # print('==============================: ', _global_dict)
def get_value(key, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

def set_token(value):
    """ 设置全局TOKEN值 """
    _global_dict['token'] = value

def get_token(defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict['token']
    except KeyError:
        return defValue

def set_order(value):
    """ 设置全局ORDER值 """
    _global_dict['token'] = value

def get_order(defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict['order']
    except KeyError:
        return defValue