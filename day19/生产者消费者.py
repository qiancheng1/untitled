def consumer():
    pass

##########################################################################
# def fun(x,*y,**z):
#     print(x,y,z)
#
# fun(1,name=2,age=3)

# def fun(x,*y,**z):
#     print(x,y,z)
#
# fun(10,2,3,4)

# def fun(*y,**z):
#     print(y,z)
#
# fun(*[1,2,3,4,5])

##########################################################################
# l1 = ["qian", 1, 2, 3, 4, 5]
# l2 = ["is", 1, 2, 3, 4, 5]
# l3 = ["good", 1, 2, 3, 4, 5]
# l4 = ["guy", 2, 3, 4, 5]
# zippped = zip(l1,l2,l3,l4)
# # print(list(zippped)[0])
# t = list(zippped)[0]
# print("_".join(t))
# print(*t)

##########################################################################
# print(bytes("中文",encoding='gbk'))
# print('zhongwen'.encode('utf-8'))

##########################################################################
# name = "big qian"
# def out(func):
#     name = "yyc"
#     func()
#     print(name)
#
# def show():
#     print(name)
#
# out(show)
# # 输出的是"big qian",不是yyc
##########################################################################
name="cls"
def out():
    name = "boduo"
    def inner():
        print(name)
        # return inner
    return inner

ret = out()
ret()
print(ret)
print(ret())