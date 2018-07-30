# import importlib
#
# m = importlib.import_module('package.Tst')
# ret = m.add(1,3)
# print(ret)

##########################################################################
# 注意两者之间的区别,这个就算你导入到了Tst模块,也是不能直接用add来直接调用的
mu = __import__("package.Tst")

ret = mu.Tst.add(1,2)
print(ret)




##########################################################################
# 导入自己模块
class FtpClient():
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def get(self):
        return self.name,self.port


import sys
modul = sys.modules[__name__]
# print这个则显示false,因为modul指的是动态导入模块.py这个py文件
# print(modul)
# print(hasattr(modul,"get"))
print(hasattr(modul.FtpClient,"get"))