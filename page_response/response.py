#!/usr/bin/env/python3
# -*- coding:utf-8 -*-

import json

import jsonpath
from common.get_log import get_log


class SaveResponse(object):
    def __init__(self):
        self.actual_response = {}

    # 保存实际响应
    def save_actual_response(self, case_key, case_response):
        """

        :param case_key:用例编号
        :param case_response:对应用例编号的实际响应
        :return:
        """
        self.actual_response[case_key] = case_response
        get_log('响应').info(f'当前字典数据{self.actual_response}')

    # 读取依赖数据
    def read_depend_data(self, depend):
        """

        :param depend: 需要依赖数据字典{"case_001":"['jsonpaht表达式1', 'jsonpaht表达式2']"}
        :return:
        """
        depend_dict = {}
        depend = json.loads(depend)
        for k, v in depend.items():
            # 取得依赖中对应case编号的值提取表达式
            try:
                for value in v:
                    # value : '$.data.id'
                    # 取得对应用例编号的实际响应结果
                    actual = self.actual_response[k]
                    # 返回依赖数据的key
                    d_k = value.split('.')[-1]
                    # 添加到依赖数据字典并返回
                    depend_dict[d_k] = jsonpath.jsonpath(actual, value)[0]
            except TypeError as e:
                get_log('响应').error(f'实际响应结果中无法正常使用该表达式提取到任何内容，发现异常{e}')

        return depend_dict