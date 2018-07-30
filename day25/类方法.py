class School:
    '''
    和java一样.类方法就是类直接调用,由于python规则限定都不是强制限定的,所以用实例也能调用,但是不建议.
    和test普通方法的区别就是普通的方法,在类中定义普通方法,实例就不能调用了.
    '''
    tag = "daxing minban gaozhong"
    @classmethod
    def info(cls):
        print(cls.tag)

    def test():
        print("for some award")



s1 = School()
s1.info()
School.info()