#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : myDriver.py
# Author: tian guang yuan
# Time  : 2020/7/23 22:00
from selenium import webdriver
from day7.utils.mySettings import driverPath, URL

class Driver:
    """浏览器驱动工具类"""
    # 初始化为 None
    _driver = None

    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        """
        获取浏览器驱动对象
        :param browser_name:
        :return:
        """
        # 如果不为空就不需要创建了
        if cls._driver is None:
            if browser_name == "Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == "Firefox":
                cls._driver = webdriver.Firefox(driverPath["Firefox"])
            # 。。。 省略其他的浏览器类型

            # cls._driver.implicitly_wait(10)
            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认网页
            cls._driver.get(URL)
            # 执行登录
            cls.__login()
        return cls._driver

    @classmethod
    def __login(cls):
        """
        私有方法，只能在类里边使用
        类外部无法使用，子类不能继承
        只在浏览器刚打开的时候登陆一次
        :return:
        """
        cls._driver.find_element_by_name("username").send_keys("libai")
        cls._driver.find_element_by_name("password").send_keys("opmsopms123")
        cls._driver.find_element_by_css_selector("button").click()


if __name__ == '__main__':
    Driver.get_driver()


