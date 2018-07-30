#授权是利用反射来实现的,getattr
class Open:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def read(self):
        pass

    def write(self):
        pass

    def __getattr__(self, item):
        print(item)

f = Open("asus","r")
f.read()