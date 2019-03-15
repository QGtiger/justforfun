from qiniu import Auth, put_file, etag
import qiniu.config
import os
from urllib.request import quote, unquote
import time

bucket_url = 'http://www.qnpic.top\\'


def qiniu_upload(warehouse, imgpath, savename):
    """
    warehouse: 存储库
    imgpath: 图片地址
    savename: 上传到七牛保存的文件名
    """
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'B4grHJfkEDxZ99R5HoYhcfI03CYAnHe1lxfmOUcg'
    secret_key = 'yP4ykoS4wad_14kMBFUvx1PvbxxZnR_zFlrkqZS3'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = warehouse
    # 上传到七牛后保存的文件名
    key = savename
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key)
    # 要上传文件的本地路径
    localfile = imgpath
    ret, info = put_file(token, key, localfile)
    # print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)


allfile = []


def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getallfile(filepath)
        else:
            allfile.append(filepath)
    return allfile


qiniu_upload('blog','D:\\blog\\argparse_ment\\1.jpg','qnpic_test.jpg')
