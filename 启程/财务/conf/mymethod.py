#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : mymethod.py
# Author: tian guang yuan
# Time  : 2020/9/24 10:17
import os
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')
class MyMethod:
    def __init__(self):
        pass

    def write_file(self, str):
        '''
        '''
        f1 = open('write.txt', 'a')
        f1.writelines(str)
        f1.flush()
        f1.close()

    def read_file(self, filename):
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

if __name__ == "__main__":

    # MyMethod().write_file(['werwerwe\n','hello world\n','mark\n'])
    thon = MyMethod()
    L = thon.read_file('E:\\songqin\\web自动化\\启程\\财务\\data\\abst.txt')
    # print(L)
    for i in L:
        print(i)
    # for i in L:
    #     # print(i.split(','))
    #     lista = i.split(',')
    #     addAbstract = {'number': lista[0], 'name': lista[1]}
    #     print(addAbstract['number'])



