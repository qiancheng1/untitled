class Room():
    def __init__(self,name,length,width,heigh):
        self.name = name
        self.length = length
        self.width = width
        self.heigh = heigh

# 相当于把函数属性变成数据属性
    @property
    def get_cal(self):
        return self.length * self.width


r1 = Room("yyc_rom",12,24,23)
print(r1.get_cal)