#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3鼠标事件.py
# Author: tian guang yuan
# Time  : 2020/7/19 21:34
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com/")
# 定位到需要悬停的元素
ele = driver.find_element_by_name("tj_briicon")
# 对定位到的元素执行鼠标悬停的操作
ActionChains(driver).move_to_element(ele).perform()
# 右键操作
ActionChains(driver).context_click(ele).perform()
# 双击
ActionChains(driver).double_click(ele).perform()

# 访问网址
driver.get("E:\songqin\web自动化\day4\\test2.html")
# 定位到需要拖动的元素
ele1 = driver.find_element_by_id("blackSquare")
# 定位到目标元素
ele2 = driver.find_element_by_id("targetEle")
#  拖动元素
ActionChains(driver).drag_and_drop(ele1, ele2).perform()








