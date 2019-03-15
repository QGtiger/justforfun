"""
author:lightfish
Time:2018.11.18
note:下载pexels图片
"""
import requests
import json
import os
from bs4 import BeautifulSoup
import math
import re

data = {
    'i': '风景',
    'from': 'AUTO',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1537680464627',
    'sign': 'c72a93599c0c533050645cbe45bfd391',
    'doctype': 'json',
    'version': 2.1,
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def YouDao():
    content = input('请输入图片的类型: ')
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(content)
    if match:
        data['i'] = content
        html = requests.post(
            'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule',
            data=data,
            headers=headers)
        html = json.loads(html.text)
        #print('翻译：'+html['translateResult'][0][0]['tgt'])
        return html['translateResult'][0][0]['tgt']
    else:
        return content


def get_page_urls(url):
    try:
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        imgs = soup.find_all('img', attrs={'class': 'photo-item__img'})
        list = []
        for img in imgs:
            list.append(img.get('data-big-src'))
        return list
    except Exception as e:
        print(e)


def downloadPic(name, pic_url, localPath, n):
    path = localPath + '/' + name + '/'
    if not os.path.exists(path):
        os.mkdir(path)
    for i, url in enumerate(pic_url[:n]):
        try:
            i = i + 1
            pic = requests.get(url, headers=headers)
            print(path + name + str(i) + '.jpg')
            with open(path + name + str(i) + '.jpg', 'wb') as f:
                f.write(pic.content)
            print('loading {} pic...'.format(str(i)))
        except Exception as e:
            print('something error')
            print(e)
            continue


def getPexelPic(search_word):
    url = 'https://www.pexels.com/search/'
    pic_num = input('请输出您要爬取的图片数(阿拉伯数字)：')
    while True:
        if pic_num.isdigit():
            break
        else:
            pic_num = input(
                'I said just input a number! :')
    page = math.ceil(int(pic_num)/30)
    url = url + search_word + '/'
    pic_urls = []
    page = int(page) + 1
    for x in range(1, int(page)):
        re_url = url + '?page=' + str(x)
        print(re_url)
        pic_urls.extend(get_page_urls(re_url))

    downloadPic(search_word, pic_urls, 'E:/PythonPic',int(pic_num))


if __name__ == '__main__':
    search_word = YouDao()
    getPexelPic(search_word)
