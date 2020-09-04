#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import config
from Command.Cmd import Cmd
from Perform.Activity import Activity


class AnalysisActivity(object):
    """解析apk活动信息类"""

    def __init__(self):
        self.activity = Activity()

    def get_activity(self):
        """
        获取当前活动最顶层的apk的包名，以此来判断要测试的apk是否已经退出或发生闪退
        :return: 返回最顶层apk包名
        """
        pattern = re.compile("[a-zA-Z0-9\\.]+/.[a-zA-Z0-9\\.]+")  # 创建模式对象
        cmd = Cmd.CMD_PACKAGE_WINDOWS if config.OS is "windows" else Cmd.CMD_PACKAGE_LINUX  # 判断是windows系统还是linux系统
        result = self.activity.perform_activity(cmd)  # 获取当前活动在最顶层的apk
        return str(pattern.findall(str(result))[0].split('/')[0])  # 解析成包名 并返回

    def get_pid(self):
        """
        获取pid
        :return: 返回对应pid获取None
        """
        cmd = Cmd.CMD_PS_WINDOWS if config.OS is "windows" else Cmd.CMD_PS_LINUX  # 判断是windows系统还是linux系统
        ps_out = self.activity.perform_pid(cmd.format(config.APP_PACKAGE)).readlines()
        for ps_line in ps_out:
            ps_items = ps_line.split(" ")
            if len(ps_items) == 0:
                return None
            count = 0
            for ps_item in ps_items:
                if ps_item is not '':
                    count = count + 1
                    if count is 2:
                        return ps_item
        return None
