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


def GetFileMd5(filename='xmltest.xml'):
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
print(filepath)
"""
我判断这个条件为空,上面我写的这个不行
用这个if not filepath.strip() 或者 if filepath.strip() == ""
None和空值是两个概念,None不是空,只不过是NaN类型,我是智障了,mdzz....
if filepath.strip(os.linesep) is None:
"""
if not filepath.strip():
    print(GetFileMd5())
else:
    print(GetFileMd5(filepath))
endtime = datetime.datetime.now()
print('运行时间：%ds' % ((endtime - starttime).seconds))
