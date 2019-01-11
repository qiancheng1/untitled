#!/usr/bin/python
# coding=utf-8

import os
import re
from pprint import pprint
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests


class qushibaikeSpider(object):
    old_url = set()
    new_url = set()

    def __init__(self, base_url):
        self.base = base_url

    def get_html_src(self,url):
        headers = {
            "User - Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        html = requests.get(url, headers=headers).text
        html.encode('gb18030')
        return html

    def get_pages(self,bsobj):
        page_urls = []
        # 获取当前套图的页面url
        '''现在这个好像有点问题,6页之后的爬不到了,其实后面还有的
        那我就查找这个<li class="next-page"><a href="5326_14.html">下一页</a></li>,看是否为空'''
        # pages = bsobj.find('div', {'class': 'pagination pagination-multi'}).findall('a', href=re.compile(".*html$"))
        pages = bsobj.find('div', {'class': 'pagination pagination-multi'}).findAll('a', href=re.compile(".*html$"))
        print(pages)
        page_urls.append(self.base)
        for page_url in pages:
            page_url = urljoin(self.base, page_url['href'])
            if page_url not in page_urls:
                page_urls.append(page_url)
        pprint('page urls is %s' % page_urls)
        return page_urls

    def html_src_parser(self, html):
        image_urls = []

        bsobj = BeautifulSoup(html, 'lxml')
        # 获取标题
        titles = bsobj.find('h1', {'class': 'article-title'}).get_text()
        print(titles)
        page_urls = self.get_pages(bsobj)


        #根据每个page下载图片
        for page in page_urls:
            print('current page is %s' % page)
            # 获取当前页的图片url
            new_html = self.get_html_src(page)
            bs = BeautifulSoup(new_html,'lxml')
            imgs = bs.find('article', {'class': 'article-content'}).findAll('img', src=re.compile(".*jpg$"))
            # self.result_output(img['src'],titles)
            for img in imgs:
                print(img['src'])
                image_urls.append(img['src'])
        pprint(image_urls)
        return image_urls,page_urls

    def result_output(self, imgs, page_urls,titles='aa'):
        count = 1
        headers = {
            "User - Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        if not os.path.isdir('qiushibaike' + os.path.sep + titles):
            os.makedirs('qiushibaike' + os.path.sep + titles)
        os.chdir('qiushibaike' + os.path.sep + titles)
        for img in imgs:
            print(img)
            req = requests.get(img, headers=headers)
            with open(titles + str(count) + '.jpg', 'wb') as f:
                f.write(req.content)
                print("保存第" + str(count) + "张图片成功")
                count += 1


if __name__ == "__main__":
    url = "https://5252ll.com/luyilu/2018/0614/5326.html"
    baike = qushibaikeSpider(url)
    src = baike.get_html_src(url)
    image_urls,page_urls = baike.html_src_parser(src)
    baike.result_output(image_urls,page_urls)
