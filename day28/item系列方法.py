class Foo:
    def __getitem__(self, item):
        print("getitem")
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print("setitem")
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("delitem")
        self.__dict__.pop(key)

f1 = Foo()
print(f1.__dict__)
# 这样的f1.调用的方式字啊内部其实是调用__getattr__,attribute属性的方式来调用的,而item是字典的方式来调用
# f1.name = "egon"
# f1.age = 24
f1["name"] = "yyc"
f1["age"] = 9000

# 不会触发系列
# del f1.name
# f1.age

del f1["name"]
f1["gender"] = "M"
print(f1["age"])
print(f1.__dict__)
