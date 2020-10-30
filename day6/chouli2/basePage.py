#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : basePage.py
# Author: tian guang yuan
# Time  : 2020/7/21 22:49
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day6.chouli2.mySettings import TIMEOUT, POLL_FREQUENCY
from day6.chouli2.myDriver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self, locator):
        """
        （显示等待）根据表达式匹配单个元素，并返回元素对象
        :param locator: 元组，第 0 个元素表示定位方法，第 1 个元素表示元素定位表达式
        :return:
        """
        # 判断元素是否存在
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 传入轮询时间
            poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        # 返回元素对象
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """
        （显示等待）根据表达式匹配元素列表，并返回元素列表
        :param locator: 元组，第 0 个元素表示定位方法，第 1 个元素表示元素定位表达式
        :return:
        """
        # 判断元素是否存在
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 传入轮询时间
            poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        # 返回元素对象
        return self.driver.find_elements(*locator)




