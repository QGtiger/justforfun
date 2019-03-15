"""
author:lightfish
time:2018.12.19
note:千千音乐的批量下载
"""
import requests
import re
import json


def get_music_resource(songid):
    search_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172047648654448286276_1545221906467&songid={}'.format(
        songid)
    response = requests.get(search_url).text
    res = re.findall('\((.*)\)', response)[0]
    res_json = json.loads(res)
    return res_json

def get_music_info(jsondata):
    songinfo = jsondata['songinfo']
    music_title = songinfo['title']
    print('歌名: ' + music_title)
    music_compose = songinfo['compose']
    print('作者: ' + music_compose)
    album_title = songinfo['album_title']
    print('专辑: ' + album_title)
    avatar = songinfo['artist_list'][0]['avatar_s300'] if songinfo['artist_list'][0]['avatar_s300'] else ''
    print('头像: ' + avatar)
    music_language = songinfo['language'] if songinfo['language'] else ''
    print('语种: ' + music_language)
    music_country = songinfo['country'] if songinfo['country'] else ''
    print('国家: ' + music_country)
    music_url = jsondata['bitrate']['file_link']
    print(music_url)
    return music_title,music_url



def music_download(filename,url):
    with open(filename+'.mp3','wb') as f:
        f.write(requests.get(url).content)



if __name__ == '__main__':
    songid = input('请输入歌曲的id: ')
    data = get_music_resource(songid)
    music_title,music_url = get_music_info(data)
    is_download = input('是否下载(y/n): ')
    if is_download.lower() == 'y':
        music_download(music_title,music_url)
        print('下载完成，Just for fun...')
    elif is_download.lower() == 'n':
        print('Just for fun')
    else:
        print('emmm,f**k')