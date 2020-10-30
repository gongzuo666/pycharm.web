#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 2隐式等待.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:40
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 设置隐式等待, 只对之后的元素定位有效
# 隐式等待默认参数是秒，如下代码，设置等待时间最大为20秒
# 当脚本执行到某个元素定位的时候，能定位就继续执行
# 如果不能定位，以轮询的方式不断判断元素能否被定位到
# 假设，在第 x 秒(x <= 20)定位到元素，就不等了，继续往下执行
# 直到超出最大等待时间，还没有定位到元素，抛出异常
driver.implicitly_wait(20)

# 访问网址
driver.get("https://m.weibo.cn/")

ele = driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div")
ele.click()

ele = driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4")
ele.click()

ele = driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1) > div > div > div > div > span.main-link.m-box.m-box-center-a > span.main-text.m-text-cut")
print(ele.text)

# driver.quit()







