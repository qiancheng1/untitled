#!/usr/bin/python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print("root is", root.tag)

# root下面第一层节点的信息
for child in root:
    print("=======>", child.tag, child.attrib, child.attrib["name"])
    # 遍历第一层节点下面的子节点
    for i in child:
        print(i.tag, i.attrib, i.text)

print("***********************************")
# 遍历root节点下面的子孙节点,注意是子孙节点都可以,不一定要子节点,能找到就可以
for node in root.iter("year"):
    print(node.tag, node.text)


# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated', 'yes')
    node.set('version', '1.0')
tree.write('test.xml')

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')