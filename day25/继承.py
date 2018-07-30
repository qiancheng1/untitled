# class Yyc:
#     def __init__(self,name):
#         self.name = name
#
#     def hit_man(self):
#         print("%s is hitting his son" % self.name)
#
#
# class Baby_Yyc(Yyc):
#     pass
#
#
# by = Baby_Yyc("baby_yyc")
# by.hit_man()

##########################################################################
# all is file
#接口实现
import abc

class All_is_file(metaclass=abc.ABCMeta):

    @abstractmethod
    def read(self):
        pass

    def wirte(self):
        pass

class mem(All_is_file):
    def read(self):
        print("this is mem file object")
