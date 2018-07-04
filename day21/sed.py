import sys


def featch(data):
    print("\033[1;43这是查询功能\033[0m")

def add():
    pass

def change():
    pass

def delete():
    pass

if __name__ == "__main__":
    print('''
    1.查询
    2.添加
    3.修改
    4.删除
    5.退出
    ''')
    msg_dict={
        "1":featch,
        "2":add,
        "3":change,
        "4":delete
    }

    while True:
        # print(msg)
        choice = input("输入选项:").strip()
        if not choice:continue
        if choice == 5:
            sys.exit(1)
            break
        data = input("data is:")
        msg_dict[choice](data)
        # if choice == 1:
        #     da = input("data is: ")
        #     msg_dict[choice](da)
        # else:
        #     msg_dict[choice]()
