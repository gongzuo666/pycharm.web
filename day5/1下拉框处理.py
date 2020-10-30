#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 1下拉框处理.py
# Author: tian guang yuan
# Time  : 2020/7/20 8:49
from selenium.webdriver.support.select import Select
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("E:\\songqin\web自动化\day5\\test.html")

# 先定位到下拉框元素
ele = driver.find_element_by_id("abc")
# # 根据 value 属性选择
# Select(ele).select_by_value("p2")
# # 根据下标选择
# Select(ele).select_by_index(3)
Select(ele).select_by_index(2)
# 根据可视文本选择
# Select(ele).select_by_visible_text("月薪三十万")




