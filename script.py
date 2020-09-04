#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
import log
import time
import logging
import config
from Base.BaseFactory import BaseFactory
from Base.Utils import DataConversionUtil
from Command.Cmd import Cmd


class Script(object):

    def __init__(self):
        self.bf = BaseFactory()  # 创建工厂类实例对象

    def test01(self):
        """
        :测试CPU+内存占用
        """
        cpu_dict = {}
        mem_dict = {}
        cpu_list = []
        mem_list = []
        time_list = []
        try:
            # bf.get_analysis_adb_cls().get_kill_server()  # 启动adb服务前先kill adb服务
            # time.sleep(3)  # kill adb 服务后需要等待一段时间才能执行adb start-server 否则很容易报错
            # logging.info('关闭adb服务成功')
            # bf.get_analysis_adb_cls().get_start_server()  # 启动adb服务
            # time.sleep(3)
            # logging.info('启动adb服务成功')
            if self.bf.get_analysis_connect_cls().get_devices():  # 查询连接
                logging.info('连接的盒子已离线，请重新连接')
                if self.bf.get_analysis_activity_cls().get_pid() is None:
                    logging.info("application is not running-->>请关机后重新启动要测试的盒子")
            time.sleep(2)
            if self.bf.get_analysis_connect_cls().get_connect_stb(Cmd.CMD_CONNECT.format(config.IP_PORT)):
                logging.info(config.IP_PORT+'-->>设备连接成功')
                while config.RUN_COUNT > 0:
                    if self.bf.get_analysis_activity_cls().get_pid() is None:
                        logging.info("application is not running-->>请启动要测试的应用")
                    else:
                        cpu = self.bf.get_analysis_cpu_cls().get_cpu_top()
                        mem = self.bf.get_analysis_memory_cls().get_memory()
                        logging.info("CPU: {}, ".format(cpu) + "mem: {}".format(str(mem)) + "KB" + "--{}MB".format(
                            int(mem / 1024)) + '--' + str(int((mem / 1024 / config.MEM_SIZE) * 100)) + "%")
                        cpu_list.append(int(cpu.strip('%')))
                        mem_list.append(int((mem / 1024 / config.MEM_SIZE) * 100))
                        z_time = datetime.datetime.now()
                        cpu_dict["{}".format(str(z_time).split('.', 1)[0])] = int(cpu.strip('%'))
                        mem_dict["{}".format(str(z_time).split('.', 1)[0])] = int((mem / 1024 / config.MEM_SIZE) * 100)
                        time_list.append(str(z_time).split('.', 1)[0])
                    config.RUN_COUNT -= 1

            else:
                logging.info("------------------盒子连接失败")
                exit(0)
        except Exception as errs:
            logging.info("执行出问题了，原因：{}".format(errs))
        finally:
            print(cpu_list)
            print(mem_list)
            print(time_list)
            print(cpu_dict)
            print(mem_dict)
            DataConversionUtil.dict_to_json_file(config.BASE_PATH+os.sep+'Data'+os.sep+'cpu_data', cpu_dict)
            DataConversionUtil.dict_to_json_file(config.BASE_PATH+os.sep+'Data'+os.sep+'mem_data', mem_dict)


if __name__ == '__main__':
    log.log()
    Script().test01()
    # BaseFactory.get_analysis_adb_cls().get_kill_server()
    # time.sleep(2)
    # BaseFactory.get_analysis_adb_cls().get_start_server()
    # time.sleep(5)
    # BaseFactory.get_analysis_connect_cls().get_connect_stb(Cmd.CMD_CONNECT.format(config.IP_PORT))
    # print(BaseFactory.get_analysis_cpu_cls().get_cpu_top())
