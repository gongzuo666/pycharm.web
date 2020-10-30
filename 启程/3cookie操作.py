#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3cookie操作.py
# Author: tian guang yuan
# Time  : 2020/7/20 8:49
from selenium import webdriver
import time

# 这两行是实现无界面的关键代码
option = webdriver.ChromeOptions()
option.add_argument('headless')

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe", chrome_options=option)
# 访问网址
driver.get("http://110.249.209.202:48080")
# 获得所有cookie信息
print(driver.get_cookies())
time.sleep(3)
# 输入用户名
driver.find_element_by_css_selector('form > div:nth-child(1) input').send_keys("guang")
# 密码
driver.find_element_by_css_selector('form > div:nth-child(2) input').send_keys("123456")
# 点击登录按钮
driver.find_element_by_css_selector("form div.el-select span.el-input__suffix").click()
time.sleep(1)
driver.find_element_by_css_selector("div.el-scrollbar ul > li:nth-child(1)").click()
driver.find_element_by_css_selector("div.el-form-item button > span").click()
# 获得登录后的所有cookie信息
print(driver.get_cookies())
driver.quit()









