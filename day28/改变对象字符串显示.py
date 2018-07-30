# print(obj)-->str(obj)--->obj.__str__()方法

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "this is __str__  %s" % self.name

    # 解释器层面的,如果没有str的话,就找repr,备胎方法
    def __repr__(self):
        return  "this is __repr__ %s" % self.name

f = Foo('ogen',33)
print(f) # str(f)-->f.__str__()

