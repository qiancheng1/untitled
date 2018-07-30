class School:
    '''
    静态方法就是相当于工具方法,在类中,在方法里面不能用类的属性.
    '''
    @staticmethod
    def tool():
        total = sum([1,2,3,4,5,6])
        return  total



print(School.tool())