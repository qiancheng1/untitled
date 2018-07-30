class Desc:
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")

class TestDesc:
    x = Desc()

kd = TestDesc()
kd.x
'''
　　① self: Desc的实例对象，其实就是TestDesc的属性x
　　② instance: TestDesc的实例对象，其实就是kd
　　③ owner: 即谁拥有这些东西，当然是 TestDesc这个类，它是最高统治者，其他的一些都是包含在它的内部或者由它生出来的
'''