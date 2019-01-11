import requests
r = requests.get('https://www.baidu.com')
#这些都是属性值
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
