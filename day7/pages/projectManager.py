#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : projectManager.py
# Author: tian guang yuan
# Time  : 2020/7/23 22:11
from day7.pages.basePage import BasePage
from day7.utils.mySettings import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ProjectManager(BasePage):
    def __init__(self, path="/project/manage"):
        """
        项目管理页面，页面类
        """
        # super(ProjectManager, self).__init__()
        super().__init__()
        self.path = URL + path

        # 以下封装页面元素寻找方法
        # 项目状态搜索选择下拉框
        self.project_status_locator = (By.NAME, "status")
        # 项目名称搜索输入框
        self.project_name_input_locator = (By.CSS_SELECTOR, "form > input")
        # 搜索按钮
        self.search_button_locator = (By.CSS_SELECTOR, "form > button.btn-primary")
        # 新建项目按钮
        self.create_project_buuton_locator = (By.CSS_SELECTOR, "a.btn.btn-success")
        # 匹配列表当中的每一个项目名称
        self.list_of_project_name_locator = (By.CSS_SELECTOR, "tbody > tr > td:nth-child(1)")
        # 匹配列表当中的每一个项目别名
        self.list_of_project_another_name_locator = (By.CSS_SELECTOR, "tbody > tr > td:nth-child(2)")

    def project_name_input_box(self):
        return self.get_element(self.project_name_input_locator)

    def search_button_box(self):
        return self.get_element(self.search_button_locator)

    def list_of_project_name_boxes(self):
        """匹配列表当中的每一个项目名称, 返回元素列表"""
        return self.get_elements(self.list_of_project_name_locator)

    def list_of_project_another_name_boxes(self):
        return self.get_elements(self.list_of_project_another_name_locator)

    def to_page(self):
        """
        访问此页面的网址
        :return:
        """
        self.driver.get(self.path)


class ProjectManagerAcction(ProjectManager):
    pass


# 创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
ProjectManagerAcctionObj = ProjectManagerAcction()









