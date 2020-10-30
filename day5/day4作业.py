#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : day4作业.py
# Author: tian guang yuan
from selenium import webdriver
import time
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("http://127.0.0.1:8088/login")
driver.implicitly_wait(5)
# 输入用户名
driver.find_element_by_name("username").send_keys("libai\topmsopms123\n")
# 输入密码
# driver.find_element_by_name("password").send_keys("opmsopms123")
# 点击登录
# driver.find_element_by_css_selector("button").click()
# 点击项目管理
driver.find_element_by_css_selector("a[href=\"/project/manage\"] > i + span").click()
# 点击新项目
driver.find_element_by_css_selector(".btn.btn-success").click()
# 输入项目名称
driver.find_element_by_name("name").send_keys("测试项目{}".format(time.strftime("%Y-%m-%d %X", time.localtime())))
# 输入项目别名
driver.find_element_by_name("aliasname").send_keys("别名：测试项目{}".format(time.strftime("%Y-%m-%d %X", time.localtime())))
# 切换iframe
eleIframe = driver.find_element_by_css_selector(".ke-edit-iframe")
driver.switch_to.frame(eleIframe)
# 输入内容
driver.find_element_by_css_selector(".ke-content").send_keys("123456")
# 切换回主界面
driver.switch_to.default_content()
# 点击提交
driver.find_element_by_css_selector("button.btn").click()
# 点击弹窗关闭按钮
driver.find_element_by_css_selector("button.close").click()



