# -*- coding:utf-8 -*-
import os
import sys
import configparser

class WXConf:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))+"\wxbot\wx.conf")

        # 基本配置
        self.baseconf = {
            # 调试模式
            'debug' : True,
            # WXBot 掉线后自动重启
            "restartOnOffline": False,
            # 是否记录日志
            'log' : True,
            # 日志文件存放位置
            'logPath' : self.cf.get("base","logPath")+'/',
            # 登录二维码保存类型 bytes,views
            'qrCodeType': 'views',
            # 登录二维码保存位置，仅当保存类型为file时启用
            'qrCodePath': self.cf.get("base","qrCodePath")+'/',
            'version': "v1.2.3",
            'help': """
[wxbot]
    启动服务：wxbot
    选项：
        -v, --version    显示版本信息
        -h, --help       帮助信息
        -r, --restart    重新登录
        -s, --stop       停止服务
[wx]
    更新：
        update group     更新群组
        update buddy     更新联系人
    查询：
        list group       查询群组
        list buddy       查询联系人
    发送：
        send group xxx xxx   发送群组消息
        send buddy xxx xxx   发送好友消息
""",
            'dbDir': self.cf.get("base","dbDir")
        }

        # 邮件配置
        self.mailconf = {
            # 邮件服务器地址
            'mailServerAddr': self.cf.get("mail","mailServerAddr"),
            # 邮件服务器端口
            'mailServerPort': self.cf.get("mail","mailServerPort"),
            # 邮件服务器密码
            'mailServerPswd': self.cf.get("mail","mailServerPswd"),
            # 发送地址
            'fromUser': self.cf.get("mail","fromUser"),
            #  接收二维码邮件地址
            'toUser': self.cf.get("mail","toUser"),
        }

        self.init = {
            'initEnd': self.cf.get("init",'initend')
        }

    def setConf(self, section, option, value):
        self.cf.set(section=section,option=option,value=value)
        try:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))+"\wxbot\wx.conf", "w+") as f:
                self.cf.write(f)
        except ImportError:
            pass
        pass


if __name__ == '__main__':
    d = WXConf()