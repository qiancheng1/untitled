class Dad():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name,self.age)

class Son(Dad):
    def __init__(self, name, age, weight):
        super().__init__(name,age)
        # 如果不用super()的话,就要像这样用
        # Dad.__init__(self,name,age)
        self.weight = weight

    # def show_info(self):
    #     print(self.name,self.age,self.weight)

s1 = Son("gaga",11,40)
s1.show_info()
