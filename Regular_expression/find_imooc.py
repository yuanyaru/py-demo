#!/usr/bin/python
#-- coding:utf-8 --

# 找到以imooc开头的行
def find_start_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc'):
            print line

#find_start_imooc('yyr.txt')

# 找到以imooc开头和以imooc结尾的行
def find_in_imooc(fname):
    f = open(fname)
    for line in f:
        #if line.startswith('imooc') and line.endswith('imooc\n'):
        if line.startswith('imooc') and line[:-1].endswith('imooc'):
            print line

find_in_imooc('yyr.txt')
