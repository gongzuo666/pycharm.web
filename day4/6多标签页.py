#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 6多标签页.py
# Author: tian guang yuan
# Time  : 2020/7/19 21:35
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)
# 点击百度热榜
driver.find_element_by_css_selector(".title-text").click()
# 获取当前所有打开的标签页句柄
all_handles = driver.window_handles
for handle in all_handles:
    driver.switch_to.window(handle)
    if driver.title == "百度搜索风云榜":
        break

# 点击小说
driver.find_element_by_css_selector("#main-nav > li:nth-child(4)").click()






