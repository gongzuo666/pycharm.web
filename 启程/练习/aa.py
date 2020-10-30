#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : aa.py
# Author: tian guang yuan
# Time  : 2020/7/22 18:29
# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
def is_element_exist(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print("元素未找到:%s" % css)
        return False
    elif len(s) == 1:
        return True
    else:
        print("找到%s个元素：%s" % (len(s), css))
        return False

