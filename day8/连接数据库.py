#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 连接数据库.py
# Author: tian guang yuan
# Time  : 2020/9/7 16:55
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='aiopms', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 使用cursor()创建游标
cursor = connection.cursor()
# 创建sql 语句
sql = "select name from pms_projects "
# 执行sql语句
cursor.execute(sql)
# 获取所有记录
results = cursor.fetchall()
# print(results)
for data in results:
    print(data)

print("------华丽分割线--------")
# 创建sql 语句
sql = '''UPDATE pms_projects
SET name = "项目管理与OA办公12"
WHERE projectid = "66562760133054464"'''
# 执行sql语句
cursor.execute(sql)
# 获取单条数据
# results = cursor.fetchone()
# print(results)

# 关闭游标连接
cursor.close()
# 关闭数据库连接
connection.close()

