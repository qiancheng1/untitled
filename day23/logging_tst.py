import json
import logging
import sys
import time

a = "4"
dic={'name':'alvin','age':23,'sex':'male'}

b = eval(a)
print(type(b))
j = json.dumps(dic)
with open("json.info","w") as f:
    f.write(j)

with open("json.info","r") as f:
    # hui baocuo
    # data = f.read()
    # print(data["name"])
    data = json.loads(f.read())
    print(data["name"])