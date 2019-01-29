# -*- coding:utf-8 -*-
import socket
import threading

__authon__ = "cfn@leapy.cn"

from wxbot import wxparse, wxserver
from wxbot import wxconf
import sys

class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        if self.threadID == 1:
            wxserver.mysocket("0.0.0.0","8088").run()
            pass
        elif self.threadID == 2:
            wxparse.parse().login()
            pass

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

class myClient():
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("0.0.0.0", "8088"))


    pass

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
        thread1 = myThread(1, "Thread-1")
        thread2 = myThread(2, "Thread-2")
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

def wxCMD():
    argv = sys.argv[-1]
    wx = wxparse.parse()
    conf = configuration()
    # 更新联系人
    if argv == 'update contact':

        pass
    pass