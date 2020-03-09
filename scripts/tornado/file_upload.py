import sys
import tornado.web
import tornado.locks
import tornado.ioloop
from tornado.options import define, options

define("port", default=18000, help="运行端口", type=int)
define("debug", default=True, help="debug模式")

current_path = sys.path[0]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("file_upload.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["file"]  # 此处的"file"对应HTML的name="file"
        response_data = {'code': 0, 'message': 'ok'}
        for file in files:
            filename = file["filename"]
            print(filename)
            with open('./temp/' + filename, 'wb') as f:
                # 文件内容保存 到'/temp/{filename}'
                f.write(file['body'])
                response_data['data'] = '{}上传成功!'.format(filename)
        self.finish(response_data)


class UploadBinaryHandler(tornado.web.RequestHandler):
    """二进制流文件"""
    def post(self):
        response_data = {'code': 0, 'message': 'ok'}
        header = self.request.headers
        content_type = header.get('Content-Type', None)
        print('content_type:{}'.format(content_type))
        if content_type.startswith('image'):  # 图片
            filename = 'aa_b.jpg'
        else:
            response_data['code'] = 101
            response_data['message'] = 'Content-Type error'
            response_data['data'] = '请选择图片进行上传'
            self.finish(response_data)
            return None
        print(filename)
        file = self.request.body
        with open('./temp/' + filename, 'wb') as f:
            f.write(file)
        response_data['data'] = "{}上传成功!".format(filename)
        self.finish(response_data)


def main():
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/upload", UploadHandler),
            (r"/upload_b", UploadBinaryHandler)
            # (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(current_path, "static")}),
            # (r"/templates/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(current_path, "templates")}),
        ],
        debug=options.debug,
    )
    app.listen(options.port)
    print("http://localhost:{}/".format(options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    """
    http://127.0.0.1:18000/
    页面内选择文件，上传文件即可；
    文件保存在./temp下
    """
    main()
