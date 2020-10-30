#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 4元素定位的另一种方法.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:22
from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get(r"E:\songqin\web自动化\day1\test.html")
ele = driver.find_element(By.TAG_NAME, "span")
# 上边一行，等价于下边一行，都可以根据 tag_name 匹配
driver.find_element_by_tag_name("span")
print(ele.text)

# 用这个方式匹配元素列表
driver.find_elements(By.TAG_NAME, "span")

driver.quit()



