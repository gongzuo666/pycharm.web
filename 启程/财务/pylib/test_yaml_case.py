#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_yaml_case.py
# Author: tian guang yuan
# Time  : 2020/10/26 16:29
import yaml
# ------------------------读文件-----------------------
# 操作yaml
def yaml_data():
    yamlDir = '../data/yaml_test.yaml'
    # # 创建文件对象
    fo = open(yamlDir, 'r', encoding="utf8")
    res = yaml.load(fo, Loader=yaml.FullLoader)
    return res
if __name__ == '__main__':
    print(yaml_data())





