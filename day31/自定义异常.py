class _ZException(BaseException):
    def __init__(self,msg):
        self.msg = msg


raise _ZException("自己定制异常")
