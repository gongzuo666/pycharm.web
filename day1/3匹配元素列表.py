#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3匹配元素列表.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:16
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get(r"E:\songqin\web自动化\day1\test.html")
# 匹配元素列表，返回所有匹配到的元素列表，如果一个都匹配不到，就返回空列表
eleSli = driver.find_elements_by_tag_name("span")
for ele in eleSli:
    print(ele.text)

# 一个都匹配不到，就返回空列表
eleSli = driver.find_elements_by_tag_name("img")
print(eleSli)





