#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : ert.py
# Author: tian guang yuan
# Time  : 2020/10/26 17:10
from 启程.财务.pylib.test_yaml_case import yaml_data
# tian = yaml_data()
for one in yaml_data():
    print(one['number'])
# print(yaml_data()[1]['number'])
