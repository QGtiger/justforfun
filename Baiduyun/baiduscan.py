"""
author:lightfish
Time:2018.11.14
note:baiduyun验证
pip install baidu-api
result = client.basicGeneral(image,options)
options = {
    #定义图像方向
    'detect_direction':'true',
    #识别的语言类型,默认中英文
    'language_type':'CHN_ENG',
    #
}
"""
from aip import AipOcr
import json
import re

class Verification(object):
    def __init__(self):
        self.App_ID = '14803626'
        self.Api_KEY = 'tKXRN1IcHysqMnL54QRNUSCA'
        self.Secret_KEY = '7KcGdv8g4WA7jO9wEzIMIaZjWGnZV9Es'
        self.client = AipOcr(self.App_ID,self.Api_KEY,self.Secret_KEY)

    def get_file_content(self,filepath):
        with open(filepath,'rb') as f:
            return f.read()

    def get_text(self):
        options={
            # 定义图像方向
            'detect_direction': 'true',
            # 识别的语言类型,默认中英文
            'language_type': 'CHN_ENG',
        }
        img = self.get_file_content(r'C:\Users\Administrator\Desktop\1.jpg')
        result = self.client.basicGeneral(img,options)
        #res = re.sub('\'','\"',str(result))
        res = result['words_result']
        for x in res:
            print(x['words'])
        #print(result['words_result'])

if __name__=='__main__':
    test = Verification()
    test.get_text()