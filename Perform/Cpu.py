#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class Cpu(object):
    """执行命令获取cpu信息"""

    def perform_top(self, cmd):
        """
        执行top命令获取cpu信息
        :param cmd:  CMD_TOP
        :return: 数据列表
        """
        out = os.popen(cmd)  #  执行top命令
        li = out.readlines()  # 读取流对象信息 返回一个列表
        out.close()  # 关闭流对象
        return li

    def perform_cpuinfo(self, cmd):
        """
        执行dumpsys cpuinfo命令获取cpu信息
        :param cmd:  'adb shell dumpsys cpuinfo {} | findstr "TOTAL"'
        :return: 数据流
        """

def getCpu():
    """
    :获取CPU占用
    """
    out = os.popen(Cmd.CMD_TOP)
    li = out.readlines()
    out.close()
    for line in li:
        if re.findall(config.APP_PACKAGE, line):
            cuplist = line.split(" ")
            if cuplist[-1].strip() == config.APP_PACKAGE:
                while '' in cuplist:  # 将list中的空元素删除
                    cuplist.remove('')
                cpu_apk = float(cuplist[2].strip('%'))
                return str(cpu_apk) + '%' if cpu_apk is not  None else "0.0%"  # 去掉百分号，返回一个float