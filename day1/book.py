#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : book.py
# Author: tian guang yuan
# Time  : 2020/7/9 20:28
from selenium import webdriver
import time
driver1 = webdriver.Chrome("E:/toos/chromedriver.exe")
# driver1.get("http://vip.ytesting.com/q.do?a&id=ff808081703da3a4017041c7a6ea00e3")
driver1.get("https://m.weibo.cn/")
# webdriver.Firefox().get("https://m.weibo.cn/")

# driver1 = webdriver.Firefox().get("https://m.weibo.cn/")
# driver1.find_element_by_id("kw").send_keys("松勤")
# driver1.find_element_by_id("su").click()

# driver.quit()








