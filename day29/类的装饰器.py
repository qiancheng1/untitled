def shell(**kwargs):
    def deco(obj):
        print("====>",obj)
        for k,v in kwargs.items():
            setattr(obj,k,v)
        return obj
    return deco

@shell(x=1,y=2)  # Foo = deco(Foo)
class Foo:
    pass


f = Foo()
print(Foo.__dict__)