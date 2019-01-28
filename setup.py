# -*- coding: utf-8 -*-

from setuptools import setup
from wxbot import wxconf
import os


with open(r"README.md","r",encoding='UTF-8') as fh:
    long_description = fh.read()

version = wxconf.WXConf().baseconf['version']

setup(
    name = 'wxbot',
    version = version,
    packages = ['wxbot', 'plugins','wxbotdb'],
    entry_points = {
        'console_scripts': [
            'wxbot = wxbot.wxcore:wxRun',
            'wx = wxbot.wxcore:wxCMD'
        ]
    },
    data_files = [
     ('wxbot', ['wxbot/wx.conf'])
    ],
    long_description= long_description,
    long_description_content_type= "text/markdown",
    install_requires= ['requests', 'apscheduler', 'setuptools'],
    description= "WXBot: A conversation robot base on Tencent's Webweixin",
    author= 'cfn',
    author_email= 'cfn@leapy.cn',
    url= 'https://github.com/ileapy/wxbot',
    keywords= ['WXBot', 'conversation robot', 'tencent', 'weixin','web', 'network', 'python', 'http'],
    classifiers= [],
)