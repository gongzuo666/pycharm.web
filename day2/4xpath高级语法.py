#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 4xpath高级语法.py
# Author: tian guang yuan
# Time  : 2020/7/16 22:33
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")

# 访问网址
driver.get("E:\\songqin\web自动化\day2\\test.html")

ele = driver.find_element_by_xpath("//p[@id=\"abd\"]")
print(ele.text)

driver.quit()





