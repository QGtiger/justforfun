'''
time:2018年9月24日 17：36
author:lightfish
爬取地址https://free-api.heweather.com/s6/weather?
和风天气api的使用
'''
import requests
import json
import pandas as pd
import pprint


def get_weather(location):
    weather_url = 'https://free-api.heweather.com/s6/weather?'
    param = {
        'location': location,
        # 'lang': 'en',
        'key': '4915b670bf6b425b8c12c88f94d21ee4'
    }
    try:
        res = requests.get(weather_url, params=param)
        weather = json.loads(res.text)
        # print(res)
        weather_daily = weather['HeWeather6'][0]['daily_forecast'][0]
        s1 = '{} {} 天气预报:'.format(weather_daily['date'], location)
        s2 = '\n白天:{}\t夜晚:{}\n最高气温:{}℃\t最低气温:{}℃\n降雨概率:{}\n\n'.format(
                weather_daily['cond_txt_d'],
                weather_daily['cond_txt_n'],
                weather_daily['tmp_max'],
                weather_daily['tmp_min'],
                weather_daily['pop'])
        lifestyle = weather['HeWeather6'][0]['lifestyle']
        s3 = '舒适度指数: {}\n指数详述: {}\n\n空气指数: {}\n指数详述: {}'.format(
                lifestyle[0]['brf'] if lifestyle[0]['brf'] else '暂无',
                lifestyle[0]['txt'],
                lifestyle[7]['brf'],
                lifestyle[7]['txt'])
        return s1+s2+s3
        # pprint.pprint(weather)

    except Exception as e:
        return 'Something error...\n'
