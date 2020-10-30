#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : bbbbb.py
# Author: tian guang yuan
# Time  : 2020/8/27 17:33
'''
name   = '小明'
age    = 16
height = 170
用一行代码，打印出如下格式的字符串
姓名=xx&年龄=xx&身高=xx

'''
'''
name = '小明'
age = 16
height = 170
print(f'姓名={name}&年龄={age}&身高={height}')
'''
list_02 = []
dict_02 = {}
for i in range(10):
    dict_02 = {'num': i}
    list_02.append(dict_02)
    pass
print("list_02内容为:\n", list_02)


