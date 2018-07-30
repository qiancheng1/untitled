def test1():
    res = 1
    return res

a = test1()

assert a == 2
# 等价于
# if a != 2:
#     raise AssertionError