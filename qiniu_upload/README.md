# Python七牛云存储库的简单集合上传和地址获取

### 1.首先你得有一些对七牛云的了解，详情[这里](https://developer.qiniu.com/kodo/sdk/1242/python)有...

### 2.接下来我就直接展示代码了=。=(是不是有点快了，Just show you the code...and learn from it yourself...)
```
from qiniu import Auth, put_file, etag
import qiniu.config
import os
from urllib.request import quote, unquote
import time

bucket_url = 'pjas65wzi.bkt.clouddn.com\\'


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

# 获取你传进图片文件夹的地址，然后进行解析，索取里面的全部img图片，并构造图片路径
def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getallfile(filepath)
        else:
            allfile.append(filepath)
    return allfile


if __name__ == '__main__':
    house = input('请输入您要存储的存储库：')
    imgfilepath = input('请输入您要发送的图片文件夹路径：')
    imgpaths = getallfile(imgfilepath)
    savenames = [i.split('\\', i.count('\\') - 1)[-1] for i in imgpaths]
    # print(savenames)
    with open('qiniuImage.txt','a') as f:
        f.write('上传图片地址：{}\n\n'.format(imgfilepath))
    for i in range(len(imgpaths)):
        try:
            qiniu_upload(house, imgpath=imgpaths[i], savename=savenames[i])
        except Exception as e:
            print(e)
            print('上传失败...')
            continue
        print('上传图片成功，地址为: {}'.format(bucket_url + quote(savenames[i])))
        with open('qiniuImage.txt', 'a') as f:
            f.write('原图片地址: {}\n'.format(imgpaths[i]))
            f.write(
                '上传至七牛云存储 {} 的地址: \n{}\n'.format(
                    house,
                    bucket_url +
                    quote(
                        savenames[i])))
            f.write('=' * 50+'\n\n')
    print('图片已经全部存储到 qiniuImage.txt 文件...')
    print('程序5秒后关闭...')
    time.sleep(5)
```

* emm，最后打开txt文件基本就直接从中获取url
![img](http://pjas65wzi.bkt.clouddn.com/qiniu_upload.jpg)
