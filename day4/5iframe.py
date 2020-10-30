#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 5iframe.py
# Author: tian guang yuan
# Time  : 2020/7/19 21:35
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("E:\songqin\web自动化\day4\\test3.html")

# 定位到你想切进去的 iframe
eleIframe = driver.find_element_by_css_selector("iframe:nth-child(3)")
# 切换到这个内嵌网页
driver.switch_to.frame(eleIframe)
# driver.switch_to_frame(eleIframe)  # 不建议使用
driver.find_element_by_id("kw").send_keys("abc")
# 切回主界面
driver.switch_to.default_content()


