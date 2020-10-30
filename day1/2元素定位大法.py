#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 2元素定位大法.py
# Author: tian guang yuan
# Time  : 2020/7/14 17:41
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get(r"E:\songqin\web自动化\day1\test.html")

"""
# 1、通过id属性定位，只返回匹配到的第一个元素，如果找不到就报错
txtEle = driver.find_element_by_id("abc")
# 获取元素的文本值
print(txtEle.text)
"""
"""
# 2、通过name属性定位，只返回匹配到的第一个元素，如果找不到就报错
driver.find_element_by_name("a1").send_keys("两家求合葬，合葬华山傍")
"""
"""
# 3、根据xpath 定位，只返回匹配到的第一个元素，如果找不到就报错
# ele = driver.find_element_by_xpath("/html/body/div/select/option[3]")
# print(ele.text)
ele = driver.find_element_by_xpath("/html/body/div/select/option")
print(ele.text)
"""
"""
# 4、根据 css 表达式定位，只返回匹配到的第一个元素，如果找不到就报错
ele = driver.find_element_by_css_selector("body > div:nth-child(3) > select > option:nth-child(3)")
print(ele.text)
"""
"""
# 5、根据链接文本定位(全匹配，不支持模糊定位)，只返回匹配到的第一个元素，如果找不到就报错
driver.find_element_by_link_text("访问百度").click()
"""
"""
# 6 根据链接文本定位(支持模糊定位)，只返回匹配到的第一个元素，如果找不到就报错
driver.find_element_by_partial_link_text("百度").click()
"""
"""
# 根据 tag_name 定位，只返回匹配到的第一个元素，如果找不到就报错
ele = driver.find_element_by_tag_name("span")
print(ele.text)
"""
# 根据 class 属性定位
ele = driver.find_element_by_class_name("a2")
print(ele.text)

driver.quit()
