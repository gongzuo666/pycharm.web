#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 2webdriver常用方法.py
# Author: tian guang yuan
# Time  : 2020/7/18 13:33
from selenium import webdriver
import time
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
"""
# 清空输入内容
ele = driver.find_element_by_id("kw")
ele.send_keys("这是文本内容")
time.sleep(3)
ele.clear()  # 和 send_keys 一样，是针对input文本框进行的操作
# 提交表单 submit()
ele.send_keys("selenium")    # 可使用 ele.send_keys("selenium\n")  \n的作用是模拟回车键
ele.submit()
"""

# 获取元素的属性值
ele = driver.find_element_by_id("su")
print(ele.get_attribute("value"))
# 检测元素是否可见
print(ele.is_displayed())
# 获取元素的文本值
print(ele.text)
# 返回元素的尺寸
print(ele.size)







