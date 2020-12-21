# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/18 8:22
# 文件名称 ： Methodes.py
# 开发工具 ： PyCharm

from Common import Request, GToken as gt
from Config.Config import Config

request = Request.Request()
config = Config()

class notify(object):

    def notify_result(self, mode, url, data, header):
        # 请求方式
        numbers = {
            0: self.get_request,
            1: self.post_request,
            2: self.post_request_multipart,
            3: self.post_request_urlencoded
        }
        method = numbers.get(mode)
        if method:
            res = method(url, data, header)
            return res
        else:
            assert AssertionError

    def get_request(self, url, data, header):
        """
        获取枪头详情信息
        :param url:
        :param data:
        :param header:
        :return:
        """
        header['token'] = gt.get_token()
        result = request.get_request(url, data, header)
        return result

    def post_request(self, url, data, header):
        """
        根据用户，枪头编号查询可用账户
        :param url:
        :param data:
        :param header:
        :return:
        """
        header['token'] = gt.get_token()
        result = request.post_request(url, data, header)
        return result

    def post_request_multipart(self, url, data, header):
        """
        获取幂等型接口调用所需的token
        :param url:
        :param data:
        :param header:
        :return:
        """
        header['token'] = gt.get_token()
        result = request.post_request_multipart(url, data, header,'file_parm', 'file', 'f_type')
        return result

    def post_request_urlencoded(self, url, data, header):
        header['token'] = gt.get_token()
        result = request.post_request_urlencoded(url, data, header)
        return result
