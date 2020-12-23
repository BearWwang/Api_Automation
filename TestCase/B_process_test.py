# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： B_process_test.py
# 开发工具 ： PyCharm
import os
from Common.Parser import parser

import allure
import pytest
from Common.Methodes import notify, request
from Config.Config import Config
from Params.params import Process
from Common import Log
from Common import Consts
from Common import Assert

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
class TestProcess(object):
    config = Config()
    noti = notify()
    log = Log.MyLog()
    data = Process()
    case_data = data.case_data
    test = Assert.Assertions()
    # ids = [
    #     " 测试：{} ==>  预期结果：状态码={} ".
    #         format(case['test_name'], case['expected']) for case in case_data
    # ]
    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Process')
    @allure.issue(config.test04_unified_url)
    @allure.testcase(config.test04_unified_url)
    # @pytest.mark.flaky(reruns=3)
    # @pytest.mark.parametrize('case', case_data, ids=ids)
    @pytest.mark.parametrize('case', case_data)
    def test_process(self, case):
        TestProcess.test_process.__doc__ = case['test_name']
        self.log.info('demo, utl={}, data={}, header={}'.format(case['url'], case['data'], case['header']))
        # 判断请求方法
        result = self.noti.notify_result(case['mode'], case['url'], case['data'], case['header'])
        self.log.info('响应结果：%s'% result )
        print(result)
        parser(result,case['parser'],case['expected'])
        # self.test.assert_in_text(result,case['expected']),True)
        allure.attach.file((BASE_PATH+'/Log/log.log'), '附件内容是： ' + '老王调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

