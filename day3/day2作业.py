#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : day2作业.py
# Author: tian guang yuan
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("https://www.vmall.com/")
# 隐式等待
driver.implicitly_wait(10)
# 获取所有的一级菜单
liSli = driver.find_elements_by_css_selector("ol.category-list > li")
for li in liSli:
    # 先打印一级菜单
    print("一级菜单", li.find_element_by_css_selector("a > span").text)
    # 鼠标悬停到一级菜单
    ActionChains(driver).move_to_element(li).perform()
    # 匹配每一个二级菜单
    liSli2 = li.find_elements_by_css_selector("li.subcate-item")
    for li2 in liSli2:
        print("\t", li2.text)
print("="*10, "分割符", "="*10)

# 向下滚动
driver.execute_script("window.scrollBy(0, 1200)")
# 找到每一个单品
liSli = driver.find_elements_by_css_selector(".span-968.fl > ul.grid-list.clearfix > li")
for li in liSli:
    # 判断标题元素文本存不存在
    if not li.find_elements_by_css_selector("span"):
        continue
    # 获取商品名称
    goodName = li.find_element_by_css_selector("div").text
    # 获取商品价格
    goodPrice = li.find_element_by_css_selector("p.grid-price").text
    # 获取标题类型
    goodType = li.find_element_by_css_selector("span").text
    print("{}: {}, 价格: {}".format(goodType, goodName, goodPrice))

driver.quit()






