import time

print(time.time())

t = time.localtime(time.time())
print(t)
print(t.tm_year)
print(time.gmtime(1234456677))

t1 = time.strftime("%Y--%m--%d: %x:%X")
print(t1)
t2 = time.strptime("2007-05-18","%Y-%m-%d")
print(t2)