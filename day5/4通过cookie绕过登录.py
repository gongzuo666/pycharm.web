#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 4通过cookie绕过登录.py
# Author: tian guang yuan
# Time  : 2020/7/20 8:49

from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("E:/toos/chromedriver.exe")
# 访问网址
driver.get("http://127.0.0.1:8088/login")

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

# 先清除所有的 cookie
driver.delete_all_cookies()
for cookie in cookieSli:
    # 添加cookie
    driver.add_cookie(cookie)

# 刷新一下页面
driver.refresh()
