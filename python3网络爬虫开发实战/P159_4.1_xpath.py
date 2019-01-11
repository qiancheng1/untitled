from lxml import etree
import pprint

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

##################################################################################

# html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//*')
# # result = html.xpath('//li/a/text()')
# # result = html.xpath('//li[@class="item-1"]//text()')
# # result = html.xpath('//li/a/@href') #这个是获取href属性值
# result = html.xpath('//li[contains(@id,"li")]../@class') #我要是找这个标签的class属性怎么找?
# pprint.pprint(result)

##################################################################################

# #根据多个属性匹配
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)

##################################################################################

#按序选择
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath("//li[1]/a/text()")
print(result)
result = html.xpath("//li[last()]/a/text()")
print(result)
result = html.xpath("//li[last()-2]/a/text()")
print(result)