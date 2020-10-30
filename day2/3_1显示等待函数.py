#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3_1显示等待函数.py
# Author: tian guang yuan
# Time  : 2020/7/16 22:11
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 3显示等待.py
# Author: tian guang yuan
# Time  : 2020/7/16 21:43
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def webElementWait(driver, timeout,lo_time,by_locate,locate):
    """

    :param driver: 浏览器驱动对象
    :param timeout: 最大等待时间
    :param lo_time: 轮询时间
    :param by_locate: 轮询时间
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

if __name__ == '__main__':
    # 创建浏览器驱动对象
    driver = webdriver.Chrome("E:/toos/chromedriver.exe")

    # 访问网址
    driver.get("https://www.baidu.com/")
    webElementWait(driver, 10, 0.5, By.ID, "kw")

















