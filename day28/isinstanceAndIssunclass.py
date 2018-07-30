class Foo:
    # 无论找不找得到都会执行,只有在raise异常的时候才会让小弟__getattr__来处理,且只有AttributeError异常才会处理.
    def __getattribute__(self, item):
        print("__getattribute__ execute")
        raise AttributeError("抛出异常")
        # raise 这个异常则小弟就不行执行了
        # raise TabError("taberror")

    def __getattr__(self, item):
        print("__getattr__ execute")


class Bar(Foo):
    pass

f1 = Foo()
f1.xxxxx

b1 = Bar()

# print(isinstance(f1,Foo))
# print(issubclass(Bar,Foo))

