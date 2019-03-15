"""
author:lightfish
time:2018.12.16
note:电影搜索功能，返回磁力链接
"""
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import quote, unquote

headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
def search_hot_mv():
    html = requests.get('http://www.minimp4.com/',headers=headers).text
    # print(html)
    soup = BeautifulSoup(html,'lxml')
    hot = str(soup.find(attrs={'class':'list-group'}))
    hot_list = re.findall('<a.*?href="(.*?)".*?</span>(.*?)</a>',hot,re.S)
    for i,j in enumerate(hot_list):
        print(str(i+1)+'. '+j[1])
    print('')
    while True:
        n = input('亲，是否查看其中的电影简介(y/n): ')
        if n.lower() == 'y':
            while True:
                mv_num = int(input('输入您想看的热门电影该序号的: '))
                if mv_num in range(1,11):
                    getintroduction(hot_list[mv_num-1][0])
                    is_getlink = int(input('是否获取该电影资源[1(y)/0(n)]:'))
                    if is_getlink ==1:
                        index = re.split(r'[/\.]',hot_list[mv_num-1][0])[-2]
                        getlink(index,hot_list[mv_num-1][1])
                        break
                    else:
                        print('不看，gun那...')
                        break
                else:
                    print('请输入正确的序号(bitch)...')
        elif n.lower() == 'n':
            print('好咧，您咧...小的这就滚...滚..滚.')
            break
        else:
            print('请输入正确的指令(son of bitch)...')


def getintroduction(url):
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    instruction = soup.find(attrs={'class':'movie-meta'})
    print(instruction.find('h1').get_text())
    for i in instruction.find_all('p'):
        print(i.get_text())
    print('电影简介: ',soup.find(attrs={'class':'movie-introduce'}).get_text())
    print('')


def getlink(index,name):
    url = 'http://www.minimp4.com/videos/resList/'+str(index)
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    list_links = soup.find_all(attrs={'class':'text-break'})
    if len(list_links) == 0:
        print('暂无资源...')
    else:
        print('由于连接过多，磁力链接存储在该目录下')
        with open(name+'下载链接.txt','w') as f:
            f.write(soup.find(attrs={'class':'resource-help'}).get_text())
            for i in list_links:
                f.write('\n'+i.get_text()+'\n')
                f.write('链接: '+i.find('a').attrs['href']+'\n\n')
                f.write('='*80)


def search_movie(url):
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    result_item = soup.find_all(attrs={'class':'movie-name'})
    if len(result_item) == 0:
        print('抱歉，你要看的内容没有找到！')
        print('比如要搜一些系列片，如哈利波特，就只搜索哈利波特，如果加上后面的版本号，可能就找不到了~')
    else:
        print('搜索资源：')
        search_name = []
        for i,j in enumerate(result_item):
            name = j.find('strong').get_text()
            print(str(i+1)+'. '+name)
            search_name.append(name)
        is_check = input('搜索结果您是否满意(y/n): ')
        if is_check.lower() == 'y':
            while True:
                num = int(input('请输入您选中的电影序号: '))
                if num in range(1,len(result_item)+1):
                    getintroduction(result_item[num-1].find('a').attrs['href'])
                    is_getlink = int(input('是否获取该电影资源[1(y)/0(n)]:'))
                    if is_getlink == 1:
                        index = re.split(r'[/\.]', result_item[num-1].find('a').attrs['href'])[-2]
                        getlink(index, search_name[num-1])
                        break
                    else:
                        print('不看，gun那...')
                        break

if __name__=='__main__':
    print('------此程序用于电影的搜索，海量资源------------')
    print('------由于版权的问题,有些片源有可能无法下载-----')

    while True:
        print('------指令1：查看热门电影-----------------------')
        print('------指令2：搜索电影---------------------------')
        print('------指令q：退出此程序-------------------------')
        instruction = input('请输入指令：')
        if instruction == '1':
            search_hot_mv()
            print('')
        if instruction == '2':
            moviename = input('请输入您要搜索的电影名称: ')
            search_url = 'http://www.minimp4.com/search?q=' + quote(moviename)
            search_movie(search_url)
            print('')
        if instruction == 'q':
            print('程序已退出...')
            break
        else:
            print('请输入正确的指令...')