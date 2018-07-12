import random

# print(random.randint(0,10))
# print(random.choice([11,22,33]))
print(random.random())
a= [1,2,3,4,5,5,5,6]
random.shuffle(a)
print(a)


#实现一个四位验证码
def auth_code():
    code = ""
    for i in range(4):
        alf = chr(random.choice([random.randint(65,90),random.randint(97,122)]))
        num = str(random.randint(0,9))
        i = random.choice([alf,num])
        code += i
    return code

code = auth_code()
print(code)