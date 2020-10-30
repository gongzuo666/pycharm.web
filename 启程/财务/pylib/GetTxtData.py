#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : GetTxtData.py
# Author: tian guang yuan
# Time  : 2020/9/24 14:04
from 启程.财务.conf.mymethod import MyMethod

def read_file(filename):
    file_list = []
    with open(filename, 'r') as read_file:
        while True:
            line = read_file.readline().strip()
            file_list.append(line)
            if not line:
                break
                pass
    for x in file_list:
        if x == '':
            file_list.remove('')
    return file_list
def adddata():
    alist = []
    L = read_file('E:\\songqin\\web自动化\\启程\\财务\\data\\abst.txt')
    for a in L:
        # print(i.split(','))
        lista = a.split(',')
        # print(lista)
        line = {'number': lista[0], 'name': lista[1]}
        alist.append(line)
    return alist

if __name__ == '__main__':
    a = adddata()
    for i in a:
        print(i)


