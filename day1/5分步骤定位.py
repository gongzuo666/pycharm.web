#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 5分步骤定位.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:27
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get(r"E:\songqin\web自动化\day1\test.html")

# 元素层级很深，路径复杂，可以分步骤定位
# 先定位到元素的父元素
ele = driver.find_element_by_tag_name("table")
ele1 = ele.find_element_by_tag_name("td")
print(ele1.text)
driver.quit()

