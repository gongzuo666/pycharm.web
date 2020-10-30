#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : day3作业.py
# Author: tian guang yuan
from selenium import webdriver
from day4.lib import webElementWait
from selenium.webdriver.common.by import By
import time

# 这两行是实现无界面的关键代码
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 实现静默模式，在电脑上不显示页面

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe", chrome_options=option)
# 访问网址
driver.get("https://www.51job.com/")
driver.implicitly_wait(5)

driver.find_element_by_css_selector("a.more").click()
# 2 输入搜索关键词 python
webElementWait(driver, 5, 0.5, By.ID, "kwdselectid").send_keys("python")
# 点击空白区域，取消输入框蒙层
driver.find_element_by_css_selector(".rtit.r1").click()
# 3 地区选择杭州
# 点击地区按钮
driver.find_element_by_id("work_position_input").click()
time.sleep(1)
# 找到已选择地区展示控件，赋值给变量
citysEle = driver.find_element_by_id("work_position_click_multiple_selected")
# 取消选中默认城市
citysEle.find_elements_by_css_selector("span.ttag")[0].click()
# 找到杭州并点击
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
# 点击确认按钮
driver.find_element_by_id("work_position_click_bottom_save").click()
# 点击历史记录
driver.find_element_by_css_selector("div.rtit.r1").click()
# 4 职能类别  计算机--》高级软件工程师
webElementWait(driver, 5, 0.5, By.ID, "funtype_click").click()
# 点击后端开发
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
# 点击高级软件工程师
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
# 点击确认按钮
driver.find_element_by_id("funtype_click_bottom_save").click()
# 5 公司性质，选外资、欧美
# 点击展开下拉框
webElementWait(driver, 5, 0.5, By.CSS_SELECTOR, "#cottype_list > input.ef").click()
# 点击国企
driver.find_element_by_css_selector("#cottype_list > div > span:nth-child(2)").click()

# 6 工作年限选择1-3年
# 点击展开下拉框
driver.find_element_by_css_selector("#workyear_list > input").click()
# 点击 1-3 年
driver.find_element_by_css_selector("#workyear_list > div > span:nth-child(3)").click()

# 7 点击确认按钮，搜索职位
driver.find_element_by_css_selector("div.btnbox > span.p_but").click()

# 8 获取职位列表并按要求打印
# 获取职位列表
jobEleSli = driver.find_elements_by_css_selector("#resultList > div.el")

for jobEle in jobEleSli:
    if "title" in jobEle.get_attribute("class"):
        continue

    infoSli = jobEle.find_elements_by_css_selector("span")
    infos = [infoEle.text for infoEle in infoSli]
    print("|".join(infos))



