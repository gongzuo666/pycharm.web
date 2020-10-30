#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : day6作业.py
# Author: tian guang yuan
from day6.mySetting import driverPath, URL
from selenium import webdriver
import requests

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
            # 执行登录
            cls.__login()
            # 刷新一下页面
            cls._driver.refresh()
        return cls._driver

    @classmethod
    def __login(cls):
        """
        私有方法, 只能在类里边使用
        类外部无法使用, 子类不能继承
        解决登录问题
        :return:
        """
        cookieSli = [{'domain': '127.0.0.1',
                      'httpOnly': False,
                      'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
                      'path': '/',
                      'secure': False,
                      'value': '1595251447'},
                     {'domain': '127.0.0.1',
                      # 'expiry': 1626787446,
                      'httpOnly': False,
                      'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
                      'path': '/',
                      'secure': False,
                      'value': '1595251447'},
                     {'domain': '127.0.0.1',
                      # 'expiry': 1626787446,
                      'httpOnly': True,
                      'name': 'beegosessionID',
                      'path': '/',
                      'secure': False,
                      'value': 'f2eeaf458f8b1ee68bdfe8a128a5690d'}]

        # 清除所有cookie
        cls._driver.delete_all_cookies()
        for cookie in cookieSli:
            # 添加 cookie
            cls._driver.add_cookie(cookie)

if __name__ == '__main__':
    Driver.get_driver()
