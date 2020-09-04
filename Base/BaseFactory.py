#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Analysis.AnalysisActivity import AnalysisActivity
from Analysis.AnalysisAdb import AnalysisAdb
from Analysis.AnalysisConnect import AnalysisConnect
from Analysis.AnalysisCpu import AnalysisCpu
from Analysis.AnalysisMemory import AnalysisMemory


class BaseFactory(object):
    """工厂类，生产各个解析类实例"""

    @classmethod
    def get_analysis_activity_cls(cls):
        return AnalysisActivity()

    @classmethod
    def get_analysis_memory_cls(cls):
        return AnalysisMemory()

    @classmethod
    def get_analysis_adb_cls(cls):
        return AnalysisAdb()

    @classmethod
    def get_analysis_cpu_cls(cls):
        return AnalysisCpu()

    @classmethod
    def get_analysis_connect_cls(cls):
        return AnalysisConnect()