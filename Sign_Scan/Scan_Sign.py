"""
author:lightfish
Time:2018.11.28
note:扫码签到
"""

from tornado import web, httpserver, ioloop
from create_qr_code import get_code_by_str
import time


class IndexPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('Hello Tornado...')
        self.render('index.html')


class CodeHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        img_handler = get_code_by_str('Hello Tornado...')
        self.write(img_handler.getvalue())


class SignHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('sign.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        department = self.get_argument('department')
        num = self.get_argument('num')
        if name and department and num:
            with open('User.txt','a') as f:
                f.write('name: {}\ndepartment: {}\nnum: {}\n{}\n'.format(name,department,num,'='*80))
            self.write('签到成功...')
            self.render('index.html')
        else:
            self.write('请填写正确的信息！！！')
            #time.sleep(3)
            self.render('sign.html')

application = web.Application([
    (r'/index', IndexPageHandler),
    (r'/qr_code', CodeHandler),
    (r'/sign', SignHandler),
])
if __name__ == '__main__':

    http_server = httpserver.HTTPServer(application)
    http_server.listen(9000)
    ioloop.IOLoop.current().start()
