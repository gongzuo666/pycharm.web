#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 登录异常判断并截图.py
# Author: tian guang yuan
# Time  : 2020/9/9 16:28
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 访问网址
driver.get("http://110.249.209.202:48080")
driver.implicitly_wait(5)
# 设置为全屏展示
driver.maximize_window()
# 登录
try:
    driver.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys("shouji")
    driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys("123456")
    driver.find_element_by_css_selector('[placeholder="请选择账套"]').click()
    driver.find_element_by_css_selector('div.el-scrollbar > div > ul > li:nth-child(1)').click()
    driver.find_element_by_css_selector('[type="button"]').click()
    ele = driver.find_element_by_css_selector('div.wrapper > ul > li')
    assert ele.text == "查看凭证"

except Exception as msg:
    print(f"异常原因{msg}")
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    t = driver.get_screenshot_as_file(f"{nowTime}s.jpg")
    print(f"截图结果：{t}")
finally:
    # 定位凭证一级模块
    ele = driver.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
    # 对定位到的元素执行鼠标悬停的操作
    ActionChains(driver).move_to_element(ele).perform()
    # 定位新增凭证
    driver.find_element_by_css_selector('body > div.el-menu--vertical > ul > li').click()
    # 点击上传单据按钮
    driver.find_element_by_css_selector('div.screen > div.positioning > button').click()
    for a in range(2):
        for i in range(20):
            driver.find_element_by_name('file').send_keys(f"D:\\aaa\\{i}.jpg")
            time.sleep(1)
    # 悬停，第一个单元格
    # ele = driver.find_element_by_css_selector('div.table > div.table-line > div:nth-child(1)')
    # # 对定位到的元素执行鼠标悬停的操作
    # ActionChains(driver).move_to_element(ele).perform()
