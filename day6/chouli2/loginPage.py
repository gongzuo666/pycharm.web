#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : loginPage.py
# Author: tian guang yuan
# Time  : 2020/7/21 22:49
from day6.chouli2.basePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self):
        """
        进一步抽离出元素定位方法
        这里只封装寻找元素的方法，不会真的找元素
        """
        # 执行父类的构造方法
        super().__init__()
        # 用户名输入框
        self.usernameInputLocator = (By.NAME, "username")
        # 密码输入框
        self.passwordInputLocator = (By.NAME, "password")
        # 登录按钮
        self.loginButtonLocator = (By.CSS_SELECTOR, "button")

    # 用户名输入框
    def usernameInputBox(self):
        return self.get_element(self.usernameInputLocator)
    # 密码输入框
    def passwordInputBox(self):
        return self.get_element(self.passwordInputLocator)

    # 登录按钮
    def loginButtonBox(self):
        return self.get_element(self.loginButtonLocator)

# 抽离出页面动作类，继承相应的页面类
class LoginPageAction(LoginPage):
    def login(self):
        """登录系统"""
        # 输入用户名
        self.usernameInputBox().send_keys("libai")
        # 输入密码
        self.passwordInputBox().send_keys("opmsopms123")
        # 点击登录按钮
        self.loginButtonBox().click()


if __name__ == '__main__':
    LoginPageAction().login()



