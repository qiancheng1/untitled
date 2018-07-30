class List(list):

    def append(self, p_object ):
        if type(p_object) is str:
            # list.append(self,p_object)
            # 下面这个方法更规范一点
            super().append(p_object)
        else:
            print("只能添加字符串类型")

    def show_middle(self):
        ret = int(len(self) / 2)
        return self[ret]

l1 = List("asussuck")
print(l1.show_middle())
# print(l1,type(l1))