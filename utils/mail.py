#!/usr/bin/env python
#-*-coding:utf-8*-
#这个工具是每日邮件提醒工具


#!/usr/bin/env python3
#coding: utf-8

import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()

class Cfg:
    #服务器配置
    s_cfg = {
        "server":"smtp.163.com",
        "port":25,
    }
    #登录设置
    l_cfg = {
        "username":"workinform@163.com",
        "password":"linhanqiu1123",
    }
    #邮箱设置
    m_cfg = {
        "sender":"workinform@163.com",
        "receiver":["linhanqiu1123@163.com"],
    }

#内容基类
class Msg:
    def __init__(self):
        pass
    @staticmethod
    def load():
        msg['Subject'] = '每日数据情况'
        msg['From'] = 'DailyStatus<workinform@163.com>'
        msg['To'] = 'linhanqiu1123@163.com'
        content = 'hedassdaasdsadd'
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        return msg
#####################################################
#娱道邮件
class YD(Msg):
    def __init__(self):
        super(YD,self).__init__()

#商道邮件
class SD(Msg):
    def __init__(self):
        super(SD,self).__init__()

#新德里新闻情况
class India(Msg):
    def __init__(self):
        super(India,self).__init__()

#####################################################
class Mail:
    def __init__(self,type):
        self.name = "默认"
        self.t = type
        self.cs = Cfg.s_cfg
        self.cl = Cfg.l_cfg
        self.cm = Cfg.m_cfg
    def load_server(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.cs["server"],self.cs["port"])
        smtp.login(self.cl["username"],self.cl["password"])
        return smtp
    def send_mail(self):
        msg = Msg.load()
        smtp = self.load_server()
        smtp.sendmail(self.cm["sender"],self.cm["receiver"],msg.as_string())
        smtp.quit()
        print("发送成功")

if __name__=="__main__":
    a = Mail("a")
    a.send_mail()
