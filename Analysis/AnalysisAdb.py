#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Perform.Adb import Adb


class AnalysisAdb(object):
    """解析adb服务启动与停止类"""

    def __init__(self):
        self.adb = Adb()

    def get_kill_server(self):
        """
        执行关闭adb服务
        :return:
        """
        self.adb.perform_kill_server()

    def get_start_server(self):
        """
        执行启动adb服务
        :return: 返回执行结果
        """
        return self.adb.perform_start_server()

