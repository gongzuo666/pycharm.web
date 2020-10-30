#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 5简单的po模式.py
# Author: tian guang yuan
# Time  : 2020/7/20 8:50
"""
登录页面，页面类
"""
from selenium import webdriver
class LoginPage:
    """登录页面，页面类"""
    def __init__(self):
        # 创建一个 driver 对象
        self.driver = webdriver.Chrome("E:/toos/chromedriver.exe")
        # self.driver = webdriver.Firefox()   火狐
        # 访问网址
        self.driver.get("http://127.0.0.1:8088/login")
        # # 用户名输入框
        # self.userInpBox = self.driver.find_element_by_name("username")
        # # 密码输入框
        # self.pwdInpBox = self.driver.find_element_by_name("password")
        # # 登录
        # self.loginButtonBox = self.driver.find_element_by_css_selector("button")
    def userInpBox(self):
        """实时获取用户名输入框"""
        return self.driver.find_element_by_name("username")

    def pwdInpBox(self):
        """实时获取密码输入框"""
        return self.driver.find_element_by_name("password")
    def loginButtonBox(self):
        """实时获取登录按钮"""
        return self.driver.find_element_by_css_selector("button")

    def login(self):
        """登录系统"""
        # 输入用户名
        self.userInpBox().send_keys("libai")
        # 输入密码
        self.pwdInpBox().send_keys("opmsopms123")
        # 点击登录按钮
        self.loginButtonBox().click()

if __name__ == '__main__':
    loginPageObj = LoginPage()
    loginPageObj.login()










