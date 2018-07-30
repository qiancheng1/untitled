# # encoding:utf-8
# class Foo:
#     def __init__(self,n):
#         self.n = n
#
#     def __iter__(self):
#         # 我这样写for循环就会报错..
#         # return self.n
#         return self
#
#     def __next__(self):
#         if self.n == 13:
#             raise StopIteration("stop iter")
#         self.n += 1
#         return self.n
#
# fly = Foo(11)
# # print(fly.__next__())
# # print(next(fly))
# # print(next(fly))
#
# for i in fly:
#     print(i)


##########################################################################

class Febb:
    def __init__(self):
        self._a = 1
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._a > 180:
            raise StopIteration("stop iter")
        self._a, self._b = self._b, self._a + self._b
        return self._a


f = Febb()
for i in  f:
    print(i)