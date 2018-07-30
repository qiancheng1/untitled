class Foo:
    def __init__(self, y):
        self.y = y

    # 调用一个对象不存在的话执行这个方法,存在的话就不执行
    def __getattr__(self, item):
        print("execute getattr")
        return "boxb"

    def __setattr__(self, key, value):
        # 会陷入死循环,设置的时候又会触发__setattr__,所以就死循环了
        # self.key = value
        print("__setattr__ execute")
        self.__dict__[key] = value

    def __delattr__(self, item):
        # 这样的情况也会发生无限递归的情况.
        # del self.item
        # 这样一步到位就好了
        self.__dict__.pop(item)

f1 = Foo(10)
# 有的时候不会触发 没有的时候才会触发此方法
# print(getattr(f1, "y"))
# print(getattr(f1, "we"))

setattr(f1,'x',66)
print(f1.__dict__)

# del f1.x  #删除的时候会触发该方法
# setattr()  #设置的时候会触发该方法


##########################################################################

class Bcon:
    def __init__(self,name):
        self.name = name


    def __getattr__(self, item):
        return "要找的属性%s不存在" % item

    def __setattr__(self, key, value):
        print("执行__setattr__ key是{0},value是{1}".format(key,value))
        self.__dict__[key] = value

    def __delattr__(self, item):
        print("正在删除")
        self.__dict__.pop(item)
        
b1 = Bcon("yyc")
print(b1.name)
print(b1.age)
b1.gender = "female"