#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 财务自动化执行.py
# Author: tian guang yuan
# Time  : 2020/8/10 11:15
import os
import time

print(time.strftime("%Y-%m-%d-%H", time.localtime()))
date = time.strftime("%Y-%m-%d-%H", time.localtime())
# 执行RF命令
# 参数-d  指定测试报告输出路径
os.system(f'robot -d rfreport_{date} -P . -V conf/cfg.py -s webUI测试 tc')
# 单独执行指定用例
# os.system(f'robot -d rfreport_{date} -P . -V conf/cfg.py -t 添加摘要 tc')


