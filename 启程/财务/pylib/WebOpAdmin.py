#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : WebOpAdmin.py
# Author: tian guang yuan
# Time  : 2020/8/24 14:37
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from 启程.财务.conf.cfg import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''
class WebOpAdmin:
    # 保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setupWebTest(self,driverType='chrome'):
        # self.cur_wd 保存 WebDriver 对象
        self.cur_wd = None
        if driverType == 'chrome':
            self.cur_wd = webdriver.Chrome()
        elif driverType == 'firefox':
            self.cur_wd = webdriver.Firefox()
        else:
            raise Exception('unknow driver type %s' % driverType)

        self.cur_wd.implicitly_wait(10)

    def tearDownWebTest(self):
        self.cur_wd.quit()

    # 定义登录方法
    def loginWebSite(self):
        self.cur_wd.get(MgrLoginUrl)
        # 设置为全屏展示
        self.cur_wd.maximize_window()
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys(user1['name'])
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys(user1['pw'])
        self.cur_wd.find_element_by_css_selector('[placeholder="请选择账套"]').click()
        self.cur_wd.find_element_by_css_selector('div.el-scrollbar > div > ul > li:nth-child(1)').click()
        self.cur_wd.find_element_by_css_selector('[type="button"]').click()

    def add_delete_Table(self):
        # 定位凭证一级模块
        ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        # 定位新增凭证
        self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(1)').click()
        # 悬停，第一个单元格
        ele = self.cur_wd.find_element_by_css_selector('div.table > div.table-line > div:nth-child(1)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        i = 0
        while True:
            if i <= 5:
                # 点击表格加图标
                addcon = self.cur_wd.find_element_by_css_selector('div.table > div.table-line > div:nth-child(5)')
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
                deletecon = self.cur_wd.find_element_by_css_selector('div.table > div.table-line > div:nth-child(6)')
                deletecon.click()
                time.sleep(1)
                j += 1
                print("点击减图标" + str(j) + "次")
            else:
                break

    def addcredentials(self):
        self.cur_wd.implicitly_wait(5)
        # # 定位凭证一级模块
        # ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
        # # 对定位到的元素执行鼠标悬停的操作
        # ActionChains(self.cur_wd).move_to_element(ele).perform()
        # # 定位新增凭证
        # self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(1)').click()
        i = 2
        j = 3
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        for a in range(2):
            # 添加摘要
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(1)').click()
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(1) input').send_keys(credentials['Abstract'])
            # 添加科目
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(2)').click()
            fele = self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(2) input')
            fele.send_keys(credentials['subject'])
            # 点击下箭头
            fele.send_keys(Keys.DOWN)
            # 回车键
            fele.send_keys(Keys.ENTER)

            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child({j})').click()
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child({j}) input').send_keys(credentials['money'])
            i += 1
            j += 1
        time.sleep(2)
        # 点击上传单据按钮
        self.cur_wd.find_element_by_css_selector('div.screen > div.positioning > button').click()
        for a in range(2):
            for i in range(2):
                self.cur_wd.find_element_by_name('file').send_keys(f"D:\\aaa\\{i}.jpg")
                time.sleep(1)
        # 点击关闭按钮
        self.cur_wd.find_element_by_css_selector('[aria-label="上传单据"] > .el-dialog__header > button').click()
        time.sleep(2)
        # 点击保存按钮
        self.cur_wd.find_element_by_css_selector('div.footer-right > button:nth-child(2) > span').click()
        # 截屏整个页面
        self.cur_wd.get_screenshot_as_file(f"../截图/凭证保存成功{nowTime}截图.png")
        time.sleep(3)
        # 点击顶部右侧箭头>
        self.cur_wd.find_element_by_css_selector('.crea-right > button:nth-child(2)').click()
        zyele = self.cur_wd.find_element_by_css_selector('div.table > div:nth-child(2) > div > div')
        assert zyele.text == credentials['expected']
        # 截屏整个页面
        self.cur_wd.get_screenshot_as_file(f"../截图/凭证断言{nowTime}截图.png")
        self.cur_wd.refresh()
    def addAbstract(self, number, name):
        self.cur_wd.implicitly_wait(10)
        # # 定位设置模块
        # ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(6)')
        # # 对定位到的元素执行鼠标悬停的操作
        # ActionChains(self.cur_wd).move_to_element(ele).perform()
        # time.sleep(2)
        # # 定位常用摘要
        # self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(4)').click()
        # 点击新增按钮
        self.cur_wd.find_element_by_css_selector('.btns > button:nth-child(1)').click()
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入摘要编码"]').send_keys(number)
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入摘要名称"]').send_keys(name)
        time.sleep(1)
        self.cur_wd.find_element_by_css_selector('span > button.el-button.el-button--primary').click()

    def DeleteAbstract(self):
        self.cur_wd.implicitly_wait(10)
        # 定位设置模块
        ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(6)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        time.sleep(2)
        # 定位常用摘要
        self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(4)').click()
        # 点击清空按钮
        self.cur_wd.find_element_by_css_selector('.btns > button:nth-child(3)').click()
        time.sleep(1)
        self.cur_wd.find_element_by_css_selector('[aria-label="清空"] > .el-dialog__footer > span > .el-button--primary').click()
'''
# ------------------------------------------------内部运行-----------------------------------------------------------
from 启程.财务.pylib.test_yaml_case import yaml_data

class WebOpAdmin:
    # 保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    cur_wd = webdriver.Chrome()

    # 定义登录方法
    def loginWebSite(self, MgrLoginUrl, name, pw):
        self.cur_wd.get(MgrLoginUrl)
        # 设置为全屏展示
        self.cur_wd.maximize_window()
        # self.cur_wd.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys(user1['name'])
        # self.cur_wd.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys(user1['pw'])
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys(name)
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys(pw)
        self.cur_wd.find_element_by_css_selector('[placeholder="请选择账套"]').click()
        time.sleep(1)
        self.cur_wd.find_element_by_css_selector('div.el-scrollbar > div > ul > li:nth-child(1)').click()
        self.cur_wd.find_element_by_css_selector('[type="button"]').click()

    # 定义新增凭证页，加图标、减图标方法
    def add_delete_Table(self):
        self.cur_wd.implicitly_wait(10)
        # 定位凭证一级模块
        ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        # 定位新增凭证
        self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(1)').click()
        # 悬停，第一个单元格
        ele = self.cur_wd.find_element_by_css_selector('div.table > div.table-line > div:nth-child(1)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        i = 0
        while True:
            if i <= 5:
                # 点击表格加图标
                addcon = self.cur_wd.find_element_by_css_selector('div.table > div.table-line > div:nth-child(5)')
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
                deletecon = self.cur_wd.find_element_by_css_selector('div.table > div.table-line > div:nth-child(6)')
                deletecon.click()
                time.sleep(1)
                j += 1
                print("点击减图标" + str(j) + "次")
            else:
                break
        self.cur_wd.refresh()

    # 定义凭证新增方法
    def AddCredentials(self):
        self.cur_wd.implicitly_wait(5)
        # # 定位凭证一级模块
        # ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
        # # 对定位到的元素执行鼠标悬停的操作
        # ActionChains(self.cur_wd).move_to_element(ele).perform()
        # # 点击新增凭证
        # self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(1)').click()
        i = 2
        j = 3
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        for a in range(2):
            # 添加摘要
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(1)').click()
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(1) input').send_keys(credentials['Abstract'])
            # 添加科目
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(2)').click()
            fele = self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child(2) input')
            fele.send_keys(credentials['subject'])
            # 点击下箭头
            fele.send_keys(Keys.DOWN)
            # 回车键
            fele.send_keys(Keys.ENTER)

            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child({j})').click()
            self.cur_wd.find_element_by_css_selector(f'div.table > div:nth-child({i}) > div:nth-child({j}) input').send_keys(credentials['money'])
            i += 1
            j += 1
        time.sleep(2)
        # 点击上传单据按钮
        self.cur_wd.find_element_by_css_selector('div.screen > div.positioning > button').click()
        for a in range(2):
            for i in range(2):
                self.cur_wd.find_element_by_name('file').send_keys(f"D:\\aaa\\{i}.jpg")
                time.sleep(1)
        # 点击关闭按钮
        self.cur_wd.find_element_by_css_selector('[aria-label="上传单据"] > .el-dialog__header > button').click()
        time.sleep(2)
        # 点击保存按钮
        self.cur_wd.find_element_by_css_selector('div.footer-right > button:nth-child(2) > span').click()
        # 截屏整个页面
        self.cur_wd.get_screenshot_as_file(f"../截图/凭证保存成功{nowTime}截图.png")
        time.sleep(3)
        # 点击顶部右侧箭头>
        self.cur_wd.find_element_by_css_selector('.crea-right > button:nth-child(2)').click()
        zyele = self.cur_wd.find_element_by_css_selector('div.table > div:nth-child(2) > div > div')
        assert zyele.text == credentials['expected']
        # 截屏整个页面
        self.cur_wd.get_screenshot_as_file(f"../截图/凭证断言{nowTime}截图.png")

    # 定义查看凭证方法
    def ListCredentials(self):
        self.cur_wd.implicitly_wait(10)
        # 定位凭证一级模块
        ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(2)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        # 点击查看凭证
        self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(2)').click()
        time.sleep(1)
        # 切换到待审核
        self.cur_wd.find_element_by_css_selector('.sell-tabs > div:nth-child(2)').click()
        time.sleep(1)
        next_button = self.cur_wd.find_element_by_css_selector('.el-pagination.is-background > ul + button')
        print(next_button.get_attribute('disabled'))
        # # 获得所有分页的数量
        # total_pages = len(self.cur_wd.find_elements_by_css_selector(".el-pagination.is-background > ul > li"))
        # print(f"total_pages is {total_pages}")
        # for i in range(total_pages):
        #     # 点击全部复选框
        #     self.cur_wd.find_element_by_css_selector('.table > ul > li > label > span').click()
        #     # 点击更多操作按钮
        #     self.cur_wd.find_element_by_css_selector('.btns > div > span').click()
        #     time.sleep(1)
        #     # 点击审核操作
        #     self.cur_wd.find_element_by_css_selector('body > ul > li:nth-child(1)').click()
        #     time.sleep(2)
        # time.sleep(5)
        # 弹出提示框，点击确定按钮
        # self.cur_wd.find_element_by_css_selector('[aria-label="提示"] > .el-dialog__footer .el-button--primary').click()

    # 定义设置模块-添加摘要方法
    def addAbstract(self):
        self.cur_wd.implicitly_wait(10)
        # 定位设置模块
        ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(6)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        time.sleep(2)
        # 定位常用摘要
        self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(4)').click()

        for one in yaml_data():
            # 点击新增按钮
            self.cur_wd.find_element_by_css_selector('.btns > button:nth-child(1)').click()
            self.cur_wd.find_element_by_css_selector('[placeholder="请输入摘要编码"]').send_keys(one['number'])
            self.cur_wd.find_element_by_css_selector('[placeholder="请输入摘要名称"]').send_keys(one['name'])
            time.sleep(1)
            self.cur_wd.find_element_by_css_selector('span > button.el-button.el-button--primary').click()
            self.cur_wd.refresh()
    def DeleteAbstract(self):
        self.cur_wd.implicitly_wait(10)
        # 定位设置模块
        ele = self.cur_wd.find_element_by_css_selector('div.sidebar-container > ul > li:nth-child(6)')
        # 对定位到的元素执行鼠标悬停的操作
        ActionChains(self.cur_wd).move_to_element(ele).perform()
        time.sleep(2)
        # 定位常用摘要
        self.cur_wd.find_element_by_css_selector('body > div.el-menu--vertical > ul > li:nth-child(4)').click()
        # 点击清空按钮
        self.cur_wd.find_element_by_css_selector('.btns > button:nth-child(3)').click()
        time.sleep(1)
        self.cur_wd.find_element_by_css_selector('[aria-label="清空"] > .el-dialog__footer > span > .el-button--primary').click()
        self.cur_wd.refresh()
if __name__ == '__main__':
    # WebOpAdmin().setupWebTest()
    # WebOpAdmin().tearDownWebTest()
    WebOpAdmin().loginWebSite("http://110.249.209.202:48080", "shouji", 123456)
    # WebOpAdmin().add_delete_Table()
    WebOpAdmin().addAbstract()
    # WebOpAdmin().add_delete_Table()
    # WebOpAdmin().ListCredentials()

