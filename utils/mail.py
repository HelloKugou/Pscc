#!/usr/bin/env python
#-*-coding:utf-8*-
#这个工具是每日邮件提醒工具


#!/usr/bin/env python3
#coding: utf-8
# coding: utf-8
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email


#列表类
class LS:
    mail_address=[
        "linhanqiu1123@163.com"
    ]
#配置类
class Cfg:
    mail_config = {
        "sender":"workinform@163.com",
        "receiver":[],
        "username":"workinform@163.com",
        "password":"linhanqiu1123",
        #smtp服务器
        "smtpserver":"smtp.163.com"
    }
    @staticmethod
    def insert_md():
        global mail_config
        for i in LS.mail_address:
            mail_config["receiver"].append(i)

    sys_config = {
        #图片地址
        "path": "/home/linhanqiu/img/1.jpg"
    }

#内容类
class Content:
    def __init__(self,id=None,word="今日数据正常，暂无反常数据产生",subject=u"每日通知"):
        self.id = id
        self.word = word
        self.subject = subject
        self.html = "<p1></p1>"
    #内容格式，其他格式还在添加
    def text(self):
        msgRoot = MIMEMultipart("related")
        msgRoot['Subject'] = Header(self.subject, 'utf-8')
        msgRoot['From'] = Header('爬虫任务情况<workinform@163.com>','utf-8')
        msgRoot['To'] = "linhanqiu1123@163.com"
        msgRoot.preamble = 'This is a multi-part message in MIME format.'
        #设置转化部分
        msgAlternative = MIMEMultipart("alternative")
        msgRoot.attach(msgAlternative)
        #添加纯文本信息，（添加模板）
        msgText = MIMEText(self.word,'plain','utf-8')
        msgAlternative.attach(msgText)
        #设定html信息，（添加模板）
        msgHtml = MIMEText(self.html,'html','utf-8')
        msgRoot.attach(msgHtml)
        #设置图片信息,（matplotlib画图）
        fp = open(Cfg.sys_config["path"], 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        return msgRoot

#邮件基类
class Mail:
    def __init__(self):
        self.cfg = Cfg.mail_config
        self.server = self.cfg["smtpserver"]
        self.sender = self.cfg["sender"]
        self.receiver = self.cfg["receiver"]
        self.username = self.cfg["username"]
        self.password = self.cfg["password"]
    def login(self):
        s = smtplib.SMTP()
        s.connect(self.server)
        s.login(self.username,self.password)
        #调式过程
        # s.set_debuglevel(1)
        s.ehlo("begin connect")
        # s.starttls()
        return s
    def send(self):
        s = self.login()
        #创建内容
        m = Content().text()
        try:
            s.sendmail(self.sender,self.receiver,m.as_string())
            print("已发送")
        except smtplib.SMTPRecipientsRefused:
            print('Recipient refused')
        except smtplib.SMTPAuthenticationError:
            print('Auth error')
        except smtplib.SMTPSenderRefused:
            print('Sender refused')
        except smtplib.SMTPException as e:
            print(e.message)
        s.quit()
    def __call__(self, *args, **kwargs):
        return self.send()

#商道邮件子类
#娱道邮件子类
if __name__=="__main__":
    mail = Mail()
    mail()