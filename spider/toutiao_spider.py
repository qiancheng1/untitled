import os

import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing import Pool

base_url = "https://www.toutiao.com/search/?"
header = {
    "referer": "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}


def get_page(offset):
    """
    offset: 0
    format: json
    keyword: 街拍
    autoload: true
    count: 20
    cur_tab: 1
    from: search_tab
    pd: synthesis
    :param offset:
    :return:
    """
    param = {
        "offset": offset,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis"
    }
    detail_url = base_url + urlencode(param)
    try:
        # ERROR:TypeError: request() got an unexpected keyword argument 'header'
        # respnse = requests.get(detail_url, header=header)
        respnse = requests.get(detail_url)
        if respnse.status_code == requests.codes.OK:
            return respnse.json()
    except requests.ConnectionError as e:
        print("error" + e.args)
        return None


def parse_page(json):
    data = json.get("data")
    if data is not None:
        for item in enumerate(data):
            # add after start
            if item.get("cell_type") is not None:
                continue
            # add after end
            title = data.get("title")
            imgs = item.get("image_list")
            for i in imgs:
                img = i.get("url")
                yield {
                    "title": title,
                    "image": "https:" + img
                }


# 主要还是接收item字典,我写复杂了
# def save_img(title, url):
#     img_dir = "toutiao" + os.path.sep + title
#     if not os.path.exists(img_dir):
#         os.mkdir(img_dir)
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             md5_name = md5(response.content)
#             img_name = md5_name + "jpg"
#             with open(img_dir + os.path.sep + img_name, "wb") as f:
#                 f.write(response.content)
#     except requests.ConnectionError as e:
#         print("error", e.args)

def save_img(item):
    img_dir = "toutiao" + os.path.sep + item.get("title")
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    try:
        response = requests.get(item.get("image"))
        if response.status_code == 200:
            file_path = img_dir + os.path.sep + "{file_name}.{file_suffix}".format(
                file_name=md5(response.content).hexdigest(),
                file_suffix='jpg'
            )
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    print('***** download image path is %s' % file_path)
                    f.write(response.content)
            else:
                print("** already download **")
    except requests.ConnectionError as e:
        print("error to save image,reason %s " % e.args)


# 目前遇到的问题,yield不断的返回,我要怎么接收parse_page返回的img的urls? 是在main里面实现还是再__main__里面实现这个?
#  --->解:你看是一个生成器,应该就想到用for循环来接收生成的参数啊, 肯定是在具体的函数里面来处理这些逻辑的
# 要怎么样才能用map把mian和别的函数关联起来?
# --->解:要关联起来,那就要在main里面把全部的逻辑都写好,因为offset就是从最开始的时候就要使用了,所以main里面要实现一整套逻辑,__main__就实现多进程就可了
# def main(offset):
#     response = get_page(offset)
#     for title, img in parse_page(response):
#         print(title, img)
#         save_img(title, img)

# 其实按照之前那么写也可以的
def main(offset):
    response = get_page(offset)
    print("qc1")
    for item in parse_page(response):
        print(item)
        save_img(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(0,8)])
    pool.map(main, groups)
    pool.close()
    pool.join()
