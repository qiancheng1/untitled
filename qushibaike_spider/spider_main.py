# coding:utf8

from qushibaike_spider import url_manager, html_output, html_downloader, html_parser


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_output.HtmlOutput()

    def crow(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("crow %d : %s" %(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 100:
                    break

                count = count + 1
            except:
                print('craw failled')
        self.outputer.output_html()



if __name__ == '__main__':
    # root_url = 'https://52zfl.vip/luyilu/2018/0922/5844.html'
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider_obj = SpiderMain()
    spider_obj.crow(root_url)