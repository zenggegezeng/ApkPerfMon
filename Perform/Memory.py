#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


class Memory(object):
    """执行命令获取内存信息"""

    def perform_meminfo(self, cmd):
        """
        行dumpsys meminfo命令获取内存信息
        :param cmd:CMD_MEMINFO_WINDOWS  或  CMD_MEMINFO_LINUX
        :return:
        """
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).stdout.readlines()


