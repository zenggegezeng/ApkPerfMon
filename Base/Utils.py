#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import time

import xlsxwriter


class AdbUtil(object):
    """
    解析ADB返回结果，
    不同设备返回的结果可能有所不同，
    主要根据返回结果进行响应的修改
    """
    USER_CPU_TEST_COUNT = 10
    USER_MEMORY_TEST_COUNT = 5
    USER_DEVICE_PHONE = "PHONE"
    USER_DEVICE_8937 = "8937"
    USER_DEVICE_TYPE = USER_DEVICE_8937

    """
    :解析应用PID
    """

    @classmethod
    def find_pid(cls, ps_out):
        ps_lines = ps_out.readlines()
        for ps_line in ps_lines:
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

    """
    :解析应用CPU
    """

    @classmethod
    def find_cpu(cls, top_out):
        for line in top_out.readlines():
            if "user" in line:
                items = line.split(" ")
                for item in items:
                    if "user" in item:
                        parts = item.split("%")
                        return parts[0]
        return None

    """
    :解析应用CPU（设备端）
    """

    @classmethod
    def find_cpu_8937(cls, top_out):
        top_lines = top_out.readlines()
        top_items = top_lines[4].split(" ")
        count = 0
        for top_item in top_items:
            if top_item is not '':
                count = count + 1
                if count is 5:
                    return int((top_item.split("%")[0]))
        return None

    """
    :解析应用USS
    :USS- Unique Set Size 进程独自占用的物理内存
    """

    @classmethod
    def find_uss(cls, procrank_out):
        procrank_items = procrank_out.split(" ")
        count = 0
        for procrank_item in procrank_items:
            if procrank_item is not '':
                count = count + 1
                if count is 5:
                    return (int)(procrank_item.split("K")[0])
        return None


class DataConversionUtil(object):
    """
    解析数据工具类
    将列表数据转换为json数据
    将字典格式数据转换为json格式
    将json'格式数据转换为列表
    将json格式数据转换为字典
    """

    @classmethod
    def list_to_json_file(cls, file_name, data):
        """
        将列表数据转换为json数据，保存在json文件中
        :return:
        """
        pass

    @classmethod
    def dict_to_json_file(cls, file_name, data):
        """
        将字典数据转换为json数据，保存在json文件中
        :return:
        """
        # result = data
        # DataConversionUtil.json_file_to_list(file_name).append(result)
        # 写入 JSON 数据
        with open('{}.json'.format(file_name), 'w') as f:
            json.dump(data, f)
        logging.info('字典数据写入--{}--文件成功'.format(file_name))

    @classmethod
    def json_file_to_list(cls, path):
        """
        将json文件数据转换为列表数据
        :return:
        """
        # papers = []  # 该数组每行都是字典数据{}
        #
        # if os.path.exists(path):
        #     file = open(path, 'r', encoding='utf-8')
        #     # 上面路径是我的json文件所在地，后面包含中文编码
        #     for line in file.readlines():
        #         dic = json.loads(line)
        #         papers.append(dic)
        # return papers
        pass

    @classmethod
    def json_file_to_dict(cls):
        """
        将json文件数据转换为字典数据
        :return:
        """
        pass


class ExcleUtil(object):
    """生成excle数据及图表工具类"""

    @classmethod
    def data_to_excle(cls, time_list, cpu_list, mem_list, mem_mb_list):
        """数据生产excle图表"""

        # 创建一个excel
        workbook = xlsxwriter.Workbook("{}.xlsx".format(time.strftime("%Y%m%d%H%M", time.localtime(time.time()))))
        # 创建一个sheet
        worksheet = workbook.add_worksheet('cpu和内存数据')
        worksheet.set_tab_color('red')  # 设置sheet标签颜色
        worksheet.set_column('A:A', 20)  # 设置A到B列的列宽为25
        # worksheet = workbook.add_worksheet("bug_analysis")

        # 自定义样式，加粗
        bold_row = workbook.add_format({
            'bold': True,  # 字体加粗
            'border': 1,  # 单元格边框宽度
            'align': 'center',  # 对齐方式
            'valign': 'vcenter',  # 字体对齐方式
            'fg_color': '#F4B084',  # 单元格背景颜色
        })

        bold_column = workbook.add_format({
            'bold': False,  # 字体加粗
            'border': 1,  # 单元格边框宽度
            'align': 'center',  # 对齐方式
            'valign': 'vcenter'  # 字体对齐方式
        })

        # --------1、准备数据并写入excel---------------
        # 向excel中写入数据，建立图标时要用到
        headings = ['Number', 'cpu(%)', 'mem(%)', 'mem(M)']
        # 写入表头
        worksheet.write_row('A1', headings, bold_row)

        # 写入数据
        worksheet.write_column('A2', time_list, bold_column)
        worksheet.write_column('B2', cpu_list, bold_column)
        worksheet.write_column('C2', mem_list, bold_column)
        worksheet.write_column('D2', mem_mb_list, bold_column)

        # --------2、生成图表并插入到excel---------------
        # 创建一个面积图(area chart)
        chart_col_cpu = workbook.add_chart({'type': 'area'})
        chart_col_mem = workbook.add_chart({'type': 'area'})

        # 配置第一个系列数据
        chart_col_cpu.add_series({
            # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
            # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
            'name': '=cpu和内存数据!$B$1',
            'categories': '=cpu和内存数据!$A$2:$A$11',
            'values': '=cpu和内存数据!$B$2:$B$11',
            'gradient': {'colors': ['red', 'green'],
                         'positions': [0, 30]},
        })

        # 配置第二个系列数据
        chart_col_mem.add_series({
            'name': '=cpu和内存数据!$C$1',
            'categories': '=cpu和内存数据!$A$2:$A$11',
            'values': '=cpu和内存数据!$C$2:$C$11',
            # 'area': {'color': 'blue'},
            'gradient': {
                'colors': ['red', 'green'],
                'positions': [0, 30]},
        })

        # 设置图表的title 和 x，y轴信息
        chart_col_cpu.set_title({'name': 'CPU占用百分比(%)'})
        chart_col_mem.set_title({'name': '内存占用百分比(%)'})
        chart_col_cpu.set_x_axis({'name': '时间(秒)'})
        chart_col_mem.set_x_axis({'name': '时间(秒)'})
        chart_col_cpu.set_y_axis({'name': '百分比(%)'})
        chart_col_mem.set_y_axis({'name': '百分比(%)'})

        #  设置图表大小
        chart_col_cpu.set_size({'width': 720, 'height': 400})
        chart_col_mem.set_size({'width': 720, 'height': 400})

        # 设置图表的风格
        chart_col_cpu.set_style(5)
        chart_col_mem.set_style(48)

        # 把图表插入到worksheet并设置偏移
        worksheet.insert_chart('A{}'.format(str(len(time_list))), chart_col_cpu, {'x_offset': 300, 'y_offset': 100})
        worksheet.insert_chart('A{}'.format(str(len(time_list))), chart_col_mem, {'x_offset': 300, 'y_offset': 400})

        workbook.close()
