#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class Adb(object):
    """操作Adb类"""

    def __init__(self):
        self._flag = False

    def perform_kill_server(self):
        """
        关闭adb服务
        :return: 无
        """
        os.system('adb kill-server')

    def perform_start_server(self):
        """
        启动adb服务
        :return:
        """
        return os.system('adb start-server')






