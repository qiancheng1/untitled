#!usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bsobj = BeautifulSoup(html,'html.parser')
# images = bsobj.findAll('img',{'src':re.compile(r'\.\./.*/img\d\.jpg')})
# bsobj.findAll(lambda tag:len(tag.attrs) == 2)
#
# for img in images:
#     print(img)


##########################################################################

random.seed(datetime.datetime.now())


def getLinks(specLinks):
    html = urlopen('https://en.wikipedia.org' + specLinks)
    bsobj = BeautifulSoup(html, 'html.parser')
    return bsobj.find('div', id='bodyContent').findAll('a', href=re.compile(r'^/wiki/((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
   newLink = links[random.randint(0,len(links)-1)].attrs['href']
   print(newLink)
   getLinks(newLink)