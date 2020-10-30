#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 2警告框处理.py
# Author: tian guang yuan
# Time  : 2020/7/19 21:34
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("E:\\songqin\web自动化\day4\\test.html")
"""
# 触发对话框
driver.find_element_by_id("bu1").click()
# 获取对话框
al = driver.switch_to.alert
al.accept()
"""
"""
# 触发确认框
driver.find_element_by_id("bu2").click()
# 获取确认框
al = driver.switch_to.alert
# 点击取消
# al.dismiss()
# 点击确定
al.accept()
"""
# 触发提示框
driver.find_element_by_id("bu3").click()
# 获取提示框
al = driver.switch_to.alert
print(al.text)
al.send_keys("今天温度很高")
al.accept()
















