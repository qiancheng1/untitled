class FtpClient():
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def get(self):
        return self.name,self.port



ftp1 = FtpClient("asus",8080)
re = hasattr(ftp1,"get")
print(re)
re = setattr(ftp1,"useful",False)
print(ftp1.__dict__)

delattr(ftp1,"name")
print(ftp1.__dict__)

