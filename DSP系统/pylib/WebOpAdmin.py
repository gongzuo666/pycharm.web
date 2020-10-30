#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : WebOpAdmin.py
# Author: tian guang yuan
# Time  : 2020/8/24 14:37
from selenium import webdriver
from random import randint
from selenium.webdriver.support.ui import Select
from 启程.财务.conf.cfg import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# ----------------------------------内部运行---------------------------------

class WebOpAdmin:
    # 保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    cur_wd = webdriver.Chrome()
    # 定义登录方法
    def loginWebSite(self, MgrLoginUrl, name, pw):
        self.cur_wd.implicitly_wait(10)
        self.cur_wd.get(MgrLoginUrl)
        # 设置为全屏展示
        self.cur_wd.maximize_window()
        # 登录
        self.cur_wd.find_element_by_css_selector('[placeholder="输入登录手机号或邮箱"]').send_keys(name)
        self.cur_wd.find_element_by_css_selector('[placeholder="输入登录密码"]').send_keys(pw)
        self.cur_wd.find_element_by_css_selector('[type="button"]').click()

    # 填写资料注册
    def Registered(self, AccountName, ContactName, phone1, portrait, NationalEmblem, IdCardNumber, ContactAddress, ReceiveName, BankAccount, phone):
        self.cur_wd.implicitly_wait(10)
        sunji = randint(1, 10)
        # 输入账户名称
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入账户名称"]').send_keys(AccountName)
        # 输入联系人姓名
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入联系人姓名"]').send_keys(ContactName)
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入联系人手机号"]').send_keys(phone1)
        # 上传人面像
        self.cur_wd.find_element_by_css_selector('.upImg > div:nth-child(1) [type="file"]').send_keys(portrait)
        # 上传国徽
        self.cur_wd.find_element_by_css_selector('.upImg > div:nth-child(2) [type="file"]').send_keys(NationalEmblem)
        # 输入身份证号码
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入身份证号码"]').send_keys(IdCardNumber)
        # 输入电子邮箱地址
        # self.cur_wd.find_element_by_css_selector('[placeholder="请输入电子邮箱地址"]').send_keys(email)
        # 输入联系地址
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入联系地址"]').send_keys(ContactAddress)
        # 输入收款方户名
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入收款方户名"]').send_keys(ReceiveName)
        # 选择开户银行
        self.cur_wd.find_element_by_css_selector('[placeholder="请选择开户银行"]').click()
        self.cur_wd.find_element_by_css_selector(f'div.el-select-dropdown.el-popper > div > div > ul > li:nth-child({sunji})').click()
        # 输入银行账号
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入银行账号"]').send_keys(BankAccount)
        # 选择开户行地址
        self.cur_wd.find_element_by_css_selector('[placeholder="请选择开户行地址"]').click()
        self.cur_wd.find_element_by_css_selector('div.el-cascader-panel > div:nth-child(1) ul > li:nth-child(4)').click()
        self.cur_wd.find_element_by_css_selector('div.el-cascader-panel > div:nth-child(2) ul > li:nth-child(2)').click()
        # 输入预留手机号
        self.cur_wd.find_element_by_css_selector('[placeholder="请输入预留手机号"]').send_keys(phone)
        self.cur_wd.find_element_by_css_selector('[type="button"]').click()
        time.sleep(10)



        # self.cur_wd.refresh()
if __name__ == '__main__':
    WebOpAdmin().loginWebSite("http://110.249.209.202:48084/#/login", "tianguangyuan@icardwow.com", "123456as")
    WebOpAdmin().Registered("永辉公司", "田光远", "15100978670", "C:\\Users\\Administrator\\Desktop\\aaa\\zz.png", "C:\\Users\\Administrator\\Desktop\\aaa\\ff.png", "130531199012062658", "石家庄长安区", "田光远", "6212260402004735799", "15100978670")


