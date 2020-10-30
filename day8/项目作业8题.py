#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 项目作业8题.py
# Author: tian guang yuan
# Time  : 2020/8/28 13:44
from selenium import webdriver
import time
import re
# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 访问网址
driver.get("https://music.163.com/")
driver.implicitly_wait(5)

driver.find_element_by_css_selector('[data-action="lock"]').click()
# 点击排行榜
driver.find_element_by_css_selector('#g_nav2 a[data-module="toplist"]').click()
time.sleep(2)

# 定位到你想切进去的 iframe
eleIframe = driver.find_element_by_id("g_iframe")
# 切换到这个内嵌网页
driver.switch_to.frame(eleIframe)

# 点击云音乐新歌榜
newele = driver.find_element_by_css_selector('.name > a[href="/discover/toplist?id=3779629"]')
newele.click()
# 点击歌名
eles = driver.find_elements_by_css_selector('tbody > tr > td.rank span.txt > a')
s = len(eles)

for i in range(s):
    eles[i].click()
    # 下滑
    js = "window.scrollTo(0,800)"
    driver.execute_script(js)  # 通过javascript设置浏览器窗口的滚动条位置
    # 获取评论作者
    author = driver.find_element_by_css_selector('.cmmts > div div.cnt >a').text
    # 获取内容
    ele = driver.find_element_by_css_selector('.cmmts > div div.cntwrap')
    ele1 = ele.get_attribute('innerHTML')
    content = re.findall('class="brand-tag brand-vip">(.*?)</div></div>', ele1)
    # 获取时间
    time1 = driver.find_element_by_css_selector('.cmmts > div div.rp > div').text
    # # 获取当前点赞数量
    ele = driver.find_element_by_css_selector('.cmmts > div div.rp')
    ele1 = ele.get_attribute('innerHTML')
    number = re.findall('</i>(.*?)</a>', ele1)[0]

    print(f'评论作者：{author} | 内容：{content} | 时间：{time1} | 点赞数量：{number}')
    # 浏览器后退
    driver.back()
    driver.refresh()
    # 定位到你想切进去的 iframe
    eleIframe = driver.find_element_by_id("g_iframe")
    # 切换到这个内嵌网页
    driver.switch_to.frame(eleIframe)
    # 重新获取一次元素
    eles = driver.find_elements_by_css_selector('tbody > tr > td.rank span.txt > a')

