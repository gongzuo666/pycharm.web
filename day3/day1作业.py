#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : day1作业.py
# Author: tian guang yuan
from selenium import webdriver
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://m.weibo.cn/")
# 隐式等待
driver.implicitly_wait(10)
# 点击搜索输入框
driver.find_element_by_css_selector("#app label > i + div").click()
# 点击微博热搜榜
driver.find_element_by_css_selector(".card.m-panel.card16.m-col-2 .card-main > div:nth-child(8)").click()
# 找到实时热点新闻列表
hotListEle = driver.find_element_by_css_selector("#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
# 找到每一行热搜标签
hotEleSli = hotListEle.find_elements_by_css_selector(".card.m-panel.card4")
for ele in hotEleSli:
    iconSli = ele.find_elements_by_css_selector(".main-text.m-text-cut + span.img")
    if iconSli:
        imgLink = iconSli[0].get_attribute("src")
        # 判断热搜类型
        if "fei" in imgLink:
            hotType = "沸"
            hotText = ele.find_element_by_css_selector(".main-text.m-text-cut")
            print("热搜类型是:{}, 热搜文本是:{}".format(hotType, hotText))
        elif "hot" in imgLink:
            hotType = "热"
            hotText = ele.find_element_by_css_selector(".main-text.m-text-cut")
            print("热搜类型是:{}, 热搜文本是:{}".format(hotType, hotText))
        elif "new" in imgLink:
            hotType = "新"
            hotText = ele.find_element_by_css_selector(".main-text.m-text-cut")
            print("热搜类型是:{}, 热搜文本是:{}".format(hotType, hotText))

driver.quit()




