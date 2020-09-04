#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Cmd:
    """定义ADB命令
    （使用了ps获取进程、top、cpuinfo获取CPU占用、procrank、meminfo获取内存占用）
    """
    #  获取pid信息
    CMD_PS_LINUX = 'adb shell ps | grep {}'
    CMD_PS_WINDOWS = 'adb shell ps | findstr {}'

    #  获取cpu信息
    CMD_TOP = 'adb shell top -m 15 -n 1'

    # CMD_PROCRANK_LINUX = 'adb shell "procrank | grep {}"'
    # CMD_PROCRANK_WINDOWS = 'adb shell "procrank | findstr {}"'

    #  内存信息
    CMD_MEMINFO_WINDOWS = 'adb shell dumpsys meminfo {} | findstr "TOTAL"'
    CMD_MEMINFO_LINUX = 'adb shell dumpsys meminfo {} | grep "TOTAL"'

    #  当前最顶层apk包名及启动名信息
    CMD_PACKAGE_WINDOWS = "adb shell dumpsys activity | findstr  mFocusedActivity"
    CMD_PACKAGE_LINUX = "adb shell dumpsys activity | grep  mFocusedActivity"

    #  启动指定activity
    CMD_START = 'adb shell am start - n {}'  # {}-->>包名+启动名

    #  连接 盒子  connect
    CMD_CONNECT = 'adb connect {}'  # ip:端口号
