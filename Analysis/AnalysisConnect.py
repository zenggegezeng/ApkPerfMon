#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Perform.Connect import Connect


class AnalysisConnect(object):
    """解析连接盒子类"""

    def __init__(self):
        self.connect = Connect()

    def get_connect_stb(self, cmd):
        """
        连接指定盒子 ip端口
        :param cmd: 要执行的命令
        :return: 返回连接成功与失败
        """
        return True if 0 == self.connect.perform_connect_stb(cmd) else False   # 解析 并返回是否连接成功   True连接成功    False连接失败

    def get_devices(self):
        """
        :return:
        """
        return True if 'offline' in self.connect.perform_devices() else False

