#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import time

from config import BASE_PATH


def log():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # logger的setLevel是最根本的
    # fh = logging.FileHandler(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + '.log')
    fh = logging.FileHandler(BASE_PATH + os.sep + "Log" + os.sep + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + '.log')
    # 如果没有这个，就不会输出到文件
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
