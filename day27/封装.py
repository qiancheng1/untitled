'''
Python中没有真正的私有属性或方法,可以在你想声明为私有的方法和属性前加上单下划线,以提示该属性和方法不应在外部调用.如果真的调用了也不会出错,但不符合规范.
双下划线开头,是为了不让子类重写该属性方法.通过类的实例化时自动转换,在类中的双下划线开头的属性方法前加上”_类名”实现.
此种写法为Python内建属性方法，最好不要在外部调用
'''
class People:
    __star = "earth"

    def __init__(self,name,number):
        self.name = name
        self.number = number


    def bridge(self):
        return self.__star


p = People("T500",11)
print(p.bridge())