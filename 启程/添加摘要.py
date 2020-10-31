#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 添加摘要.py
# Author: tian guang yuan
# Time  : 2020/9/17 17:20
from selenium import webdriver
# from 启程.登录 import lgoin
from selenium.webdriver.common.action_chains import ActionChains
import time

# 创建浏览器驱动对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 登录
# 访问网址
driver.get("http://110.249.209.202:48080")
driver.implicitly_wait(5)
# 设置为全屏展示
driver.maximize_window()
# 登录
driver.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys("shouji")
driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys("123456")
driver.find_element_by_css_selector('[placeholder="请选择账套"]').click()
driver.find_element_by_css_selector('div.el-scrollbar > div > ul > li:nth-child(1)').click()
driver.find_element_by_css_selector('[type="button"]').click()
# 定位设置模块
ele = driver.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(6)')
# 对定位到的元素执行鼠标悬停的操作
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# 定位常用摘要
driver.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(4)').click()

# 点击新增按钮
driver.find_element_by_css_selector('.btns > button:nth-child(1)').click()
driver.find_element_by_css_selector('[placeholder="请输入摘要编码"]').send_keys("1001")
driver.find_element_by_css_selector('[placeholder="请输入摘要名称"]').send_keys("摘要1")
time.sleep(1)
driver.find_element_by_css_selector('span > button.el-button.el-button--primary').click()
# # 点击清空按钮
# driver.find_element_by_css_selector('.btns > button:nth-child(3)').click()
# time.sleep(1)
# driver.find_element_by_css_selector('[aria-label="清空"] > .el-dialog__footer > span > .el-button--primary').click()
print("成功了有")
time.sleep(5)
driver.quit()
prin("成功了有231388888888888888")
