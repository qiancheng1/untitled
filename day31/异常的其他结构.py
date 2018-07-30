try:
    data = input(">>>请输入内容:")
    print(int(data))
except AttributeError as e:
    print(e)
except ValueError as e:
    print("--->",e)
else:
    print("没有异常则执行这步")
finally:
    print('最后总归执行这一步')


##########################################################################
# 主动触发异常

try:
    raise ValueError("value is error")
except ValueError as e:
    print("raise-->",e)
