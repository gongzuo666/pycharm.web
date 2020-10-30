#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : lib.py
# Author: tian guang yuan
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def webElementWait(driver, timeout, lo_time, by_locate, locate):
    """
    :param driver: 浏览器驱动对象
    :param timeout: 最大等待时间
    :param lo_time: 轮询时间
    :param by_locate: 元素定位方法
    :param locate: 元素定位表达式
    :return:
    """
    # 每隔 0.5 秒检查一次，最多等待 10 秒
    ele = WebDriverWait(driver, timeout, lo_time).until(
        EC.visibility_of_element_located(
            (by_locate, locate)
        )
    )
    return ele