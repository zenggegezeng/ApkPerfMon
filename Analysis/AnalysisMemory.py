#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import config
from Command.Cmd import Cmd
from Perform.Memory import Memory


class AnalysisMemory(object):
    """解析内存信息类"""

    def __init__(self):
        self.memory = Memory()

    def get_memory(self):
        """
        获取某个apk占用内存大小
        :return: 返回占用内存的大小
        """
        cmd = Cmd.CMD_MEMINFO_WINDOWS if config.OS is "windows" else Cmd.CMD_MEMINFO_LINUX  # 判断是windows系统还是linux系统
        str_out = map(str, self.memory.perform_meminfo(cmd.format(config.APP_PACKAGE)))  # 执行命令 获取apk的占用内存信息
        number = []
        for i in str_out:
            number.append(int(re.findall('\d+', i)[0]))  # 正则匹配出字符串中的数字列表，按选择列表[0]的数字大写排序
        return number[0] if len(number) > 0 and number[0] > 0 else 0
