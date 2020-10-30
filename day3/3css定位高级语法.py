#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3css定位高级语法.py
# Author: tian guang yuan
# Time  : 2020/7/18 13:33
from selenium import webdriver
import time
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
# driver.get("https://www.baidu.com/")
#
# driver.find_element_by_css_selector("#kw").send_keys("123456")

# 访问网址
driver.get("E:\\songqin\web自动化\day3\\test1.html")

ele = driver.find_elements_by_css_selector("#a1 p")
for one in ele:
    print(one.text)



