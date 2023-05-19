# -*- coding: utf-8 -*-
# Time : 2023/5/9 21:39
# Author : xx
# File : log.py
# Desc :

import logging

#创建日志器
logger=logging.getLogger()
# 设置日志器的级别
logger.setLevel(logging.INFO)
#定义处理器的格式
format=logging.Formatter('%(asctime)s  %(filename)s[line:%(lineno)d]%(levelname)s  %(message)s')  #设置格式   %[line:%(lineno)d] 代码所在的行
#创建处理器
fh=logging.FileHandler( r'D:\pycharm\B-web_selenium\selenium_day4\log\log.txt',mode='a',encoding='utf-8')
#设置处理器的级别
fh.setLevel(logging.INFO)
#设置处理器的格式
fh.setFormatter(format)     #设置什么样的格式存储
#添加到日志器
logger.addHandler(fh)     #处理器加载到日志器
