#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : myDriver.py
# Author: tian guang yuan
# Time  : 2020/7/21 22:48
from selenium import webdriver
from day6.chouli2.mySettings import driverPath, URL

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
            if browser_name =="Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name =="Firefox":
                cls._driver = webdriver.Firefox(driverPath["Firefox"])
            # 。。。 省略其他的浏览器类型

            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认网页
            cls._driver.get(URL)
        return cls._driver
