#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 1控制浏览器操作.py
# Author: tian guang yuan
# Time  : 2020/7/18 13:31
from selenium import webdriver
import time
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
driver.get("https://www.taobao.com/")
# 浏览器后退
driver.back()
time.sleep(3)
# 浏览器前进
driver.forward()
time.sleep(3)
# 刷新界面
driver.refresh()
# 设置浏览器的高度与宽度，参数数字的单位是像素点
driver.set_window_size(700, 700)
time.sleep(3)
# 设置为全屏展示
driver.maximize_window()
time.sleep(3)
# 设置最小化
driver.minimize_window()
time.sleep(3)













