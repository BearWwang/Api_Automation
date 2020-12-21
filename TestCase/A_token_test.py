# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： A_token_test.py
# 开发工具 ： PyCharm
import os
import allure
import pytest
from Common.Methodes import notify
from Config.Config import Config
from Common import Request, Log
from Common import Consts
from Common import Assert
from Params.params import Basic

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestBasic(object):
    log = Log.MyLog()
    data = Basic()
    case_data = data.case_data
    request = Request.Request()
    test = Assert.Assertions()
    config = Config()
    noti = notify()

    ids = [
        "测试：{}".
            format(case['test_name']) for case in case_data
    ]
    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Basic')
    @allure.issue('https://baidu.com')
    @allure.testcase('https://baidu.com')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('case', case_data, ids=ids)
    def test_login(self,case):
        """
        小程序登录
        """
        self.log.info('demo, utl={}, data={}, header={}'.format(case['url'], case['data'], case['header']))
        if case['method'] == 'post_request_urlencoded':
            result = self.request.post_request_urlencoded(case['url'], case['data'], case['header'])
            # 写入配置文件
            self.config.set_conf('parameter', 'token', result['data']['token'])
            assert self.test.assert_text(result['status'], 0)
            self.log.info('配置文件中token ={}'.format(self.config.get_conf('parameter', 'token')))
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '老王调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


