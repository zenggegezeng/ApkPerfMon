#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


class Activity(object):
    """活动类"""

    def perform_activity(self, cmd):
        """
        执行dumpsys activity命令获取当前正在活动的apk，最顶层的
        :param cmd: CMD_PACKAGE_WINDOWS  或  CMD_PACKAGE_LINUX
        :return: 数据流
        """
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()


    def perform_pid(self, cmd):
        """
        执行ps 根据包名获取pid，用pid是否存在判断apk是否在启动状态中
        :param cmd:CMD_PS_WINDOWS  或 CMD_PS_LINUX
        :return: 数据流
        """
        return os.popen(cmd)
