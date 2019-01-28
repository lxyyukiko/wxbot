# -*- coding:utf-8 -*-
__authon__ = "cfn@leapy.cn"

from wxbot import wxparse
from wxbot import wxconf
import sys

class configuration:
    def __init__(self):
        self.wconf = wxconf.WXConf()

    def check(self):
        if self.wconf.init['initEnd'] == '0':
            print("第一次运行，请配置必要的程序执行文件：")
            self.wconf.setConf("base", "dbDir", input("数据存放目录："))
            self.wconf.setConf("mail", "mailServerAddr", input("SMTP地址："))
            self.wconf.setConf("mail", "mailServerPort", input("SMTP端口："))
            self.wconf.setConf("mail", "mailServerPswd", input("SMTP密钥："))
            self.wconf.setConf("mail", "fromUser", input("邮件发送方："))
            self.wconf.setConf("mail", "toUser", input("邮件接收地址："))
            self.wconf.setConf("init", "initend", "1")
            if self.wconf.init['initEnd'] == '1':
                print("配置成功")


def wxRun():
    argv = sys.argv[-1]
    wx = wxparse.parse()
    conf = configuration()
    if argv == '-v' or argv == '--version':
        print(conf.wconf.baseconf['version'])
    elif argv == '-h' or argv == '--help':
        print(conf.wconf.baseconf['help'])
    elif argv == '-q' or argv == '--quit':
        wx.QuitLogin()
    else:
        conf.check()
        wx.login()