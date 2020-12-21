# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Email.py
# 开发工具 ： PyCharm

"""
封装发送邮件的方法

"""
import os
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Common import Consts
from Common import Log
from Config.Config import Config


class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendMail(self,report_file):
        with open(report_file, "rb") as f:
            mail_body = f.read()
        msg = MIMEMultipart()
        stress_body = Consts.STRESS_LIST
        result_body = Consts.RESULT_LIST
        body2 = 'Hi，all \n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
        mail_body2 = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告"+"_"+tm, 'utf-8')
        msg['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        msg.attach(mail_body2)
        att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename = "report.html"'
        msg.attach(att)
        try:
            try:
                smtp = smtplib.SMTP()
                smtp.connect(self.config.smtpserver)
                smtp.login(self.config.username, self.config.password)
            except:
                smtp = smtplib.SMTP_SSL(self.config.smtpserver, 25)
                smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
            smtp.quit()
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")
        else:
            print("发送成功")
            self.log.info("邮件发送成功")

def get_report_file(report_path):

    lists = os.listdir(report_path)
    lists.sort(key = lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告到>>report>>目录：'+ lists[-1])

    report_file = os.path.join( report_path, lists[-1])
    return report_file