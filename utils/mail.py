
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

import aiomysql
import asyncio
import json
import numpy as np
import matplotlib.pyplot as plt
import time
#创建数据库conn
async def get_conn():
    pool = await aiomysql.create_pool(
        host="127.0.0.1",
        port=3306,
        db="test",
        user="root",
        password="",
        charset="utf8",
        loop=loop)
    conn = await pool.acquire()
    return conn

#####################################################
#娱道邮件
class YD(Msg):
    def __init__(self):
        super(YD,self).__init__()
        self.sql = "select source,count(*)as c  from yd_new group by source ORDER by c desc;"
    async def read_f(self):
        conn = await get_conn()
        async with conn.cursor() as cor:
            await cor.execute(self.sql)
            r = await cor.fetchall()
            print(type(r[0][0]))
            return r
    #生成格式化text
    async def load_data(self):
        msg['Subject'] = '每日数据情况'
        msg['From'] = 'DailyStatus<workinform@163.com>'
        msg['To'] = 'linhanqiu1123@163.com'
        content = await self.read_f()
        #格式化成字符串
        content = json.dumps(dict(zip((i[0] for i in content),(i[1] for i in content))))
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        return msg
    async def load_data1(self):
        msg['Subject'] = '每日数据情况'
        msg['From'] = 'DailyStatus<workinform@163.com>'
        msg['To'] = 'linhanqiu1123@163.com'
        content = await self.read_f()
        x = [i[0] for i in content]
        y = [i[1] for i in content]
        n = 8
        index = np.arange(n)
        width = 0.35
        plt.bar(index,y,width)
        plt.xlabel("类型")
        plt.ylabel("数量")
        plt.xticks(index+width,x)
        timea = time.strftime("%Y-%m-%d",time.localtime())
        plt.savefig(str(time)+"娱道.jpg")

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
    def __init__(self,type=None):
        """
        :param type:int(1,2,3,4)-(默认，娱道数据，商道数据，新德里数据)
        """
        self.name = "邮件发送"
        if not type:
            self.t = 1
        else:
            self.t = type
        if self.t ==1:
            self.m = Msg()
        elif self.t ==2:
            self.m = YD()
        elif self.t ==3:
            self.m = SD()
        elif self.t ==4:
            self.m = India()
        self.cs = Cfg.s_cfg
        self.cl = Cfg.l_cfg
        self.cm = Cfg.m_cfg
    def load_server(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.cs["server"],self.cs["port"])
        smtp.login(self.cl["username"],self.cl["password"])
        return smtp
    async def send_mail(self):
        msg = await self.m.load_data()
        smtp = self.load_server()
        smtp.sendmail(self.cm["sender"],self.cm["receiver"],msg.as_string())
        smtp.quit()
        print("发送成功")

if __name__=="__main__":
    # a = Mail("a")
    # a.send_mail()
    try:
        import uvloop
        loop = asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)
    except:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(Mail(2).send_mail())
    loop.close()
