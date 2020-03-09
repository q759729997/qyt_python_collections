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
        for file in files:
            filename = file["filename"]
            print(filename)
            with open('./temp/' + filename, 'wb') as f:
                # 文件内容保存 到'/temp/{filename}'
                f.write(file['body'])
        self.write("<p>{}上传成功!</p>".format(filename))


def main():
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/upload", UploadHandler),
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
