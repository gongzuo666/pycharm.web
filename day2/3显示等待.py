#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3显示等待.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:43
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")

# 访问网址
driver.get("https://m.weibo.cn/")

ele = driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div")
ele.click()
# 每隔 0.5 秒检查一次，最多等待 10 秒
ele = WebDriverWait(driver, 10, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4")
    )
)
ele.click()











