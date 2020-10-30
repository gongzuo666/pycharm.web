#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 4键盘事件.py
# Author: tian guang yuan
# Time  : 2020/7/19 21:34
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 访问网址
driver.get("https://www.baidu.com/")

ele = driver.find_element_by_id("kw")
ele.send_keys("selenium")
time.sleep(3)
# ctrl + a 全选操作
ele.send_keys(Keys.CONTROL, "a")
time.sleep(3)
# 下键操作
ele.send_keys(Keys.DOWN)

# ctrl + x 剪切操作
# ele.send_keys(Keys.CONTROL, "x")
# ctrl + v 黏贴操作
# ele.send_keys(Keys.CONTROL, "v")
# # 退格键
# ele.send_keys(Keys.BACK_SPACE)
# # 空格键
# ele.send_keys(Keys.SPACE)
# # 回车键
# ele.send_keys(Keys.ENTER)
# # esc 键
# ele.send_keys(Keys.ESCAPE)



