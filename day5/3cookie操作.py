#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3cookie操作.py
# Author: tian guang yuan
# Time  : 2020/7/20 8:49
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("http://127.0.0.1:8088/login")
# 获得所有cookie信息
print(driver.get_cookies())
# 输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 点击登录按钮
driver.find_element_by_css_selector("button").click()
# 获得登录后的所有cookie信息
print(driver.get_cookies())
driver.quit()









