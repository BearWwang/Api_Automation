# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： contest.py
# 开发工具 ： PyCharm
import pytest
from py.xml import html


def pytest_html_report_title(report):
    report.title = "任我充Test04环境"


def pytest_configure(config):
    config._metadata.clear()
    # 添加接口地址与项目名称
    config._metadata['接口地址'] = "test04-dz-unified-gateway.iot.renwochong.com"
    config._metadata['项目名称'] = "小程序"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 任我充平台测试中心")])
    prefix.extend([html.p("测试人员: 老王")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop(-1)  # 删除link列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop(-1)  # 删除link列


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # 如果你生成的是web ui自动化测试，请把下面的代码注释打开，否则无法生成错误截图
    # if report.when == 'call' or report.when == "setup":
    #     xfail = hasattr(report, 'wasxfail')
    #     if (report.skipped and xfail) or (report.failed and not xfail):  # 失败截图
    #         file_name = report.nodeid.replace("::", "_") + ".png"
    #         screen_img = capture_screenshot()
    #         if file_name:
    #             html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
    #                    'onclick="window.open(this.src)" align="right"/></div>' % screen_img
    #             extra.append(pytest_html.extras.html(html))
    #     report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid  # 解决乱码
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


#
#
# def capture_screenshot():
#     '''截图保存为base64'''
#     return driver.get_screenshot_as_base64()
def pytest_collection_modifyitems(session, items):
    # print(type(items))
    # print("收集到的测试用例:%s" % items)
    # sort排序，根据用例名称item.name 排序
    items.sort(key=lambda x: x.name)
    for item in items:
        print("用例名:%s" % item.name.encode("utf-8").decode("unicode_escape"))
