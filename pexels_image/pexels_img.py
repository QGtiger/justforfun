'''
time:2018年9月23日
author:lightfish
爬取网址https://www.pexels.com
'''
import requests
from lxml import etree
import json
import os
from bs4 import BeautifulSoup

data={
    'i':'风景',
    'from':'AUTO',
    'to':'en',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1537680464627',
    'sign':'c72a93599c0c533050645cbe45bfd391',
    'doctype':'json',
    'version':2.1,
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'false'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
def YouDao():
    content = input('请输入你要的图片类型：')
    data['i'] = content
    html = requests.post('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule', data=data,
                         headers=headers)
    html = json.loads(html.text)
    return html['translateResult'][0][0]['tgt']

def get_page_urls(url):
    try:
        html=requests.get(url,headers=headers).text
        #print(html)
        soup=BeautifulSoup(html,'html.parser')
        #print(soup)
        imgs=soup.find_all('img',attrs={'class':'photo-item__img'})
        #print(imgs)
        list=[]
        for img in imgs:
            list.append(img.get('data-big-src'))
        return list
    except Exception as e:
        print(e)


def downloadPic(name,pic_url,localPath):
    path=localPath+'/'+name+'/'
    if not os.path.exists(path):
        os.mkdir(path)
    for i,url in enumerate(pic_url):
        try:
            i = i + 1
            pic=requests.get(url,headers=headers)
            print(path+name+str(i)+'.jpg')
            with open(path+name+str(i)+'.jpg','wb') as f:
                f.write(pic.content)
            print('loading {} pic...'.format(str(i)))
        except Exception as e:
            print('something error')
            print(e)
            continue



def getPexelPic(search_word):
    url='https://www.pexels.com/search/'
    page=input('请输出您要爬取的图片页数(阿拉伯数字)：')
    while 1:
        if page.isdigit():
            break
        else:
            page=input('Son of bitch! I said what? I said just input a number! :')

    url=url+search_word+'/'
    pic_urls=[]
    #print(url)
    page=int(page)+1
    #print(type(int(page)))
    for x in range(1,int(page)):
        re_url=url+'?page='+str(x)
        print(re_url)
        pic_urls.extend(get_page_urls(re_url))

    downloadPic(search_word,pic_urls,'E:/PythonPic')





if __name__=='__main__':
    search_word=YouDao()
    getPexelPic(search_word)

