#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 登录.py
# Author: tian guang yuan
# Time  : 2020/8/27 16:51
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

# 创建浏览器驱动对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)

def lgoin(url,name,paw):
    # 访问网址
    driver.get(url)
    # 设置为全屏展示
    driver.maximize_window()
    # 登录
    driver.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys(name)
    driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys(paw)
    # 截屏整个页面
    driver.get_screenshot_as_file(f"./截图/denglu.png")
    driver.find_element_by_css_selector('[placeholder="请选择账套"]').click()
    driver.find_element_by_css_selector('div.el-scrollbar > div > ul > li:nth-child(1)').click()
    driver.find_element_by_css_selector('[type="button"]').click()

def add_delete_Table():
    # 定位凭证一级模块
    ele = driver.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
    # 对定位到的元素执行鼠标悬停的操作
    ActionChains(driver).move_to_element(ele).perform()
    # 定位新增凭证
    driver.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(1)').click()
    # 悬停，第一个单元格
    ele = driver.find_element_by_css_selector('div.table > div.table-line > div:nth-child(1)')
    # 对定位到的元素执行鼠标悬停的操作
    ActionChains(driver).move_to_element(ele).perform()
    i = 0
    while True:
        if i <= 5:
            # 点击表格加图标
            addcon = driver.find_element_by_css_selector('div.table > div.table-line > div:nth-child(5)')
            addcon.click()
            time.sleep(1)
            i += 1
            print("点击加图标" + str(i) + "次")
        else:
            break
    j = 0
    while True:
        if j <= 6:
            # 点击表格减图标
            deletecon = driver.find_element_by_css_selector('div.table > div.table-line > div:nth-child(6)')
            deletecon.click()
            time.sleep(1)
            j += 1
            print("点击减图标" + str(j) + "次")
        else:
            break

def addcredentials(Abstract, subject, money, expected):
    # 定位凭证一级模块
    ele = driver.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
    # 对定位到的元素执行鼠标悬停的操作
    ActionChains(driver).move_to_element(ele).perform()
    # 定位新增凭证
    driver.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(1)').click()
    i = 2
    j = 3
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    for a in range(2):
        # 添加摘要
        driver.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(1)').click()
        driver.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(1) input').send_keys(Abstract)
        # 添加科目
        driver.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(2)').click()
        fele = driver.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(2) input')
        fele.send_keys(subject)
        # 点击下箭头
        fele.send_keys(Keys.DOWN)
        # 回车键
        fele.send_keys(Keys.ENTER)

        driver.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child({j})').click()
        driver.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child({j}) input').send_keys(money)
        i += 1
        j += 1
    time.sleep(2)
    # 点击上传单据按钮
    driver.find_element_by_css_selector('div.screen > div.positioning > button').click()
    for a in range(2):
        for i in range(20):
            driver.find_element_by_name('file').send_keys(f"D:\\aaa\\{i}.jpg")
            time.sleep(1)
    # 点击关闭按钮
    driver.find_element_by_css_selector('[aria-label="上传单据"] > .el-dialog__header > button').click()
    time.sleep(2)
    # 点击保存按钮
    driver.find_element_by_css_selector('div.footer-right > button:nth-child(2) > span').click()
    # 截屏整个页面
    driver.get_screenshot_as_file(f"./截图/凭证保存成功{nowTime}截图.png")
    time.sleep(5)
    # 点击顶部右侧箭头>
    driver.find_element_by_css_selector('.crea-right > button:nth-child(2)').click()
    zyele = driver.find_element_by_css_selector('div.table > div:nth-child(2) > div > div')
    assert zyele.text == expected
    # 截屏整个页面
    driver.get_screenshot_as_file(f"./截图/凭证断言{nowTime}截图.png")



if __name__ == '__main__':
    lgoin("http://110.249.209.202:48080", "shouji", "123456")
    # add_delete_Table()
    # addcredentials("下雨了20200917", "负债", "333\n", "下雨了20200917")
    driver.quit()




