class School():
    def __init__(self,name,addr,price):
        self.name = name
        self.addr = addr
        self.price = price

    @property
    def get_price(self):
        return self.price

    @classmethod
    def get_affr(self):
        return self.addr


s1 = School("tsinghua",'beijing',10)
s2 = School("Sahikto","Tokyo",10101011)