#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


class Connect(object):
    """操作连接盒子类"""

    def perform_connect_stb(self, cmd):
        """
        一次连接单个机顶盒
        :param cmd:
        :return: 返回是否连接成功
        """
        # 执行命令
        # connect = out.readlines()  # 读取流对象信息 返回一个列表
        # out.close()  # 关闭流对象
        return os.system(cmd)

    def perform_connect_stb_list(self, *ips):
        """
        次连接多个机顶盒
        :param ips: 机顶盒的ip，元组形式
        :return: 返回已连接盒子的个数
        """

    def perform_devices(self):
        """
        显示已连接的机顶盒
        :return: 返回数据流
        """
        return subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True).stdout.readlines()
