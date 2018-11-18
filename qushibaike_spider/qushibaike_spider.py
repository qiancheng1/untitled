# coding:utf8
from urllib.request import urlopen

from bs4 import BeautifulSoup


class QBSpiderMain(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def url_manager(self):
        pass

    def html_downloader(self, url):
        try:
            page = urlopen(url)
            raw_data = page.read()
        except:
            print('open url %s failed' % url)
            return raw_data

    def html_parser(self, url, page):
        soup = BeautifulSoup(page, 'html.parser', from_encoding='gbk')
        new_urls = self._craw_new_urls(url,soup)
        new_data = self._craw_new_data(url,soup)
        return new_urls, new_data

    def _craw_new_urls(self,url,s):
        pass

    def _craw_new_data(self,url,s):
        pass

    def imager_output(self):
        pass

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def crow(self, url):
        count = 1
        self.new_urls.add_new_url(url)
        while self.new_urls.has_new_url():
            try:
                new_url = self.new_urls.get_new_url()
                raw_html = self.html_downloader(new_url)
                # 返回爬取的新的url和图片信息(url)的字典
                urls, html_cont = self.html_parser(new_url, raw_html)
                self.new_urls.add_new_urls(urls)
                self.imager_output(html_cont)
                count = count + 1

                if count == 10:
                    break
            except:
                print('crow failed')


if __name__ == "__main__":
    root_url = 'https://52zfl.vip/luyilu/2018/0927/5868.html'
    sp_obj = QBSpiderMain()
    sp_obj.crow(root_url)
