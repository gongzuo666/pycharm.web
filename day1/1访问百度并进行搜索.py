#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 1访问百度并进行搜索.py
# Author: tian guang yuan
# Time  : 2020/7/14 14:47
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
print(driver.get_cookies())
# 找到输入搜索框
inpEle = driver.find_element_by_id("kw")
driver.find
inpEle.send_keys("松勤")
# 找到搜索按钮
sEle = driver.find_element_by_id("su")
sEle.click()
# # 退出浏览器
driver.quit()










