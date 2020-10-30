#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 1获取断言信息.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:33
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
# 获取当前页面标题
# assert driver.title == "百度一下，你就知道"
# 获取当前页面 URL
# print(driver.current_url)
# assert driver.current_url == "https://www.baidu.com/"

# 获取标签对之间的文本信息
ele = driver.find_element_by_css_selector("#hotsearch-content-wrapper > li:nth-child(2) > a > span.title-content-title")
assert ele.text == "以张艺兴为灵感小说将拍电影"



driver.quit()