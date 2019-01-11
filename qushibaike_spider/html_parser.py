import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        soup = BeautifulSoup(html_cont,'lxml',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.findAll('a',href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            full_url = urljoin(page_url,new_url)
            new_urls.add(full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        new_data = {}
        '''
         dd lemmaWgt-lemmaTitle-title
        < div
        class ="lemma-summary" label-module="lemmaSummary" >
        < div
        class ="para" label-module="para" > Python 是一门有条理的和强大< / div >
        < / div >
        '''
        new_data['url'] = page_url
        node_title = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        new_data['title'] = node_title.get_text()
        node_summary = soup.find('div',{"class":"lemma-summary"})
        new_data['summary']= node_summary.get_text()

        return new_data