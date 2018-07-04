import random
import time

alex_dic={"name":None,"passwd":None}

# def auth_func(func):
#     global alex_dic
#     def wapper(*args,**kwargs):
#         name = input("请输入名字:")
#         passwd = input("请输入密码:")
#         if alex_dic["name"] and alex_dic["passwd"]:
#             if name == "sd" and passwd == "123":
#                 alex_dic["name"] = name
#                 alex_dic["passwd"] = passwd
#                 res = func(*args,**kwargs)
#                 print(alex_dic["name"], alex_dic["passwd"])
#                 return res
#         else:
#             res = func(*args,**kwargs)
#             # print(alex_dic["name"], alex_dic["passwd"])
#             return res
#     return wapper
current_dict = {"name":None,"login_stat":False}

def auth_func(func):
    def wapper(*args,**kwargs):
        name = input("name:")
        passwd = input("password:")
        start_time = time.time()
        mtime = random.random(1, 10)
        print("delay time is {0}".format(mtime))
        with open("passwd","r",encoding="utf-8") as f:
            for line in f:
                data_dict = eval(line)
                if name in data_dict and passwd == data_dict[name]:
                    res = func(*args,**kwargs)
                    return res
            else:
                print("no such name or pass is incorrect")
        return wapper


@auth_func
def home(name):
    print("hello welcome to  home! %s"% name)

@auth_func
def shopping_car():
    print("购物车里面有{0},{1},,{2}".format("奶茶","mm","ww"))




home('yyc')
shopping_car()