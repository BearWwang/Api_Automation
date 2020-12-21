# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： tools.py
# 开发工具 ： PyCharm
"""
读取yaml测试数据

"""

import yaml
import os
import os.path


def parse():
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_ya = BASE_PATH + '/Params/Param'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'rb') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []
            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list
        return _page_list


if __name__ == '__main__':
    list =[]
    lists = GetPages.get_page_list()
