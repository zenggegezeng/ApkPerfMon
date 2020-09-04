#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import config
from Command.Cmd import Cmd
from Perform.Cpu import Cpu


class AnalysisCpu(object):
    """解析CPU信息类"""

    def __init__(self):
        self.cpu = Cpu()

    def get_cpu_top(self):
        """
        解析top命令获取cpu信息
        :return: 返回cpu使用率百分比
        :param cmd: 传入要执行的top命令
        """
        result = self.cpu.perform_top(Cmd.CMD_TOP)
        if config.APP_PACKAGE in str(result):  # 如果返回的结果中没有
            for line in result:
                if re.findall(config.APP_PACKAGE, line):
                    cuplist = line.split(" ")
                    if cuplist[-1].strip() == config.APP_PACKAGE:  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
                        while '' in cuplist:  # 将list中的空元素删除
                            cuplist.remove('')
                        return str(cuplist[2])
        return '0%'
