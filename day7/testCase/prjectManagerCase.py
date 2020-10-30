#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : prjectManagerCase.py
# Author: tian guang yuan
# Time  : 2020/7/23 22:52
from day7.pages.projectManager import ProjectManagerAcctionObj
import unittest
import time


class PrjectManagerCase(unittest.TestCase):

    def test_indistinct_search(self):
        """
        模糊查询测试用例，当我搜索一个项目的时候
        搜索出来的列表，别名或项目名称中至少有一个包含我搜索的文本
        :return:
        """
        ProjectManagerAcctionObj.to_page()

        time.sleep(1)

        """1 选定文本，输入并搜索"""
        project_name = "OA"
        ProjectManagerAcctionObj.project_name_input_box().send_keys(project_name)
        ProjectManagerAcctionObj.search_button_box().click()

        """2 获取项目名称列表，获取项目别名列表"""
        # 获取项目名称列表
        project_name_sli = ProjectManagerAcctionObj.list_of_project_name_boxes()
        # 获取别名列表
        project_another_name_sli = ProjectManagerAcctionObj.list_of_project_another_name_boxes()

        """3 断言验证，搜索出来的列表，别名或项目名称中至少有一个包含我搜索的文本"""
        for projectName in project_name_sli:
            as1 = project_name in project_another_name_sli[project_name_sli.index(projectName)].text
            as2 = project_name in projectName.text

            self.assertTrue(as1 or as2)


if __name__ == '__main__':
    unittest.main()







