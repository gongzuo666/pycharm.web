#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 1窗口截图.py
# Author: tian guang yuan
# Time  : 2020/7/19 21:34
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
# 设置为全屏展示
driver.maximize_window()
# 截屏整个页面
driver.get_screenshot_as_file("./截图/all.png")
# 截屏，截取单个元素
ele = driver.find_element_by_id("form")
ele.screenshot("./截图/ele.png")

driver.quit()









