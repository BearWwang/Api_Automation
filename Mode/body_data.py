# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/18 8:19
# 文件名称 ： body_data.py
# 开发工具 ： PyCharm

def json_to_get(json_data):
    get_data = str(json_data)
    get_data = get_data.replace(',', '&').replace('\'', '').replace('"', '').replace(':', '=').replace(' ', '').replace(
        '{', '').replace('}', '')
    return get_data
