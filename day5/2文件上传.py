#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 2文件上传.py
# Author: tian guang yuan
# Time  : 2020/7/20 8:49
from selenium import webdriver
import win32com.client
import time
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://tinypng.com/")

# 触发文件上传的操作
driver.find_element_by_css_selector(".icon").click()
sh = win32com.client.Dispatch("WScript.shell")
time.sleep(3)
# 漫无目的的，没有灵性的敲击键盘（我不管你对不对，反正我就是敲)
sh.Sendkeys("C:\\Users\Administrator\Desktop\\20190812164957.png\n")











