#!/usr/bin/python
# -*- coding: utf-8 -*-
import fileinput
import os
import re
import sys

'''
        替换原理：
        1、open打开文件 采用r+模式
        2、读取文件内容
        3、将文件读写指针移位到文件开始位置 seek(0,0) 这才是关键,不然就在后面添加
        4、遍历文件内容，并替换指定指定字符串
        5、重新写入文件
        其他：我在window下执行的，在Linux执行原理一样

'''
with open("test.xml", "r+") as hand:
    content = []
    for line in hand:
        # print(line,sep="")
        if re.search(r"hello", line) is not None:
            newline = re.sub(r"hello", "NIHAO", line)
            content.append(newline)
        elif re.search(r"cheng", line):
            newline = re.sub(r"cheng", "qian~~~~~", line)
            content.append(newline)
        elif re.search(r"hava",line):
            newline = re.sub(r"\s*i","#i",line)
            content.append(newline)
        else:
            content.append(line)
    hand.seek(0, 0)
    hand.writelines(content)

# other
# with open("test.xml", "r+") as hand:
#     datalist = hand.readlines()  #data is list, type error
#     hand.seek(0,0)
#     for data in datalist:
#         newlines = re.sub(r"hello", "NIHAO", data)
#         # print(newlines)
#         hand.write(newlines)

##########################################################################
# #donot work!
# if os.path.exists("./test.xml"):
#     for ih in fileinput.input("test.xml"):
#         if re.findall(r"hello",ih):
#             newline = re.sub(r"hello","NIHAO",ih)
#             sys.stdout.write(newline)
#         else:
#             print("nothing found")

'''
#读取最后一行,like:
tail -n 1 target.file
'''
