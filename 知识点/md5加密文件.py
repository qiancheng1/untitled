# coding=utf-8

import hashlib
import os
import datetime

'''
资料:
https://blog.csdn.net/shanliangliuxing/article/details/10115397

/*
* wind-mobi md5sum checklist
*/
6ddaa05902bacd5547646229fc4c95bd *sbl1.mbn
我们的md5的格式
'''

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
    myhash.update(b)
    f.close()
    return myhash.hexdigest()

filepath = input('请输入文件路径：')

# 输出文件的md5值以及记录运行时间
starttime = datetime.datetime.now()
print(GetFileMd5(filepath))
endtime = datetime.datetime.now()
print('运行时间：%ds' % ((endtime - starttime).seconds))
