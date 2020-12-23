# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/23 13:21
# 文件名称 ： Parser.py
# 开发工具 ： PyCharm
import inspect

from Common import Log, Assert

test = Assert.Assertions()

log = Log.MyLog()

def retrieve_name(var):
    """
    核心： 把变量名转换成 字符串
    :param var:
    :return:
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def parser(response_data, parser_data, expected_data):
    """
    读取yaml文件进行解析 断言，核心 把字符串转换可执行变量
    :param response_data:
    :param parser_data:
    :param expected_data:
    :return:
    """
    a = ''.join(retrieve_name(response_data))
    for x, y in dict(parser_data).items():
       result = test.assert_text(eval(a+parser_data[x]), expected_data[x])
    return result
