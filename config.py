#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

#  操作平台，有操作平台决定要执行的命令
OS = None

# 当前文件的文件夹路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

#  包名列表
APP_PACKAGE_LIST = ["com.miguplayerdemo.phone", ]
# 当前活动的包名
APP_PACKAGE = 'com.miguplayerdemo.phone'
#  包名加启动名
# APP_PACKAGE_ACTIVITY = []  #  如果要自动启动apk则需要保存包名+启动名

#  要统计的次数
RUN_COUNT = 10

#  每隔多少秒统计一次
INT_TIME = 5

# 要连接的盒子，列表格式
CONNECT_LIST = []

#  厂商提供给apk的总内存大小 MB
MEM_SIZE = 1000

#  IP:端口号  adb连接时使用
IP_PORT = '192.168.1.102:5555'


