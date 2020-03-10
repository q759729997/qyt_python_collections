"""
Socket Tornado
参考资料：https://blog.csdn.net/qq_33961117/article/details/94624357
在线socket测试：http://ws.douqq.com/
"""
import tornado.ioloop
from tornado.websocket import WebSocketHandler

from tornado.options import define, options
define("port", default=18000, help="run on the given port", type=int)


class IndexHandler(WebSocketHandler):

    def open(self, *args, **kwargs):
        print("WebSocket opened")

    def on_message(self, message):
        """处理client发送的消息"""
        print(message)
        self.write_message('received:{}'.format(message))

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        """允许跨域通讯问题"""
        return True


if __name__ == "__main__":
    """
    访问链接：
    ws://127.0.0.1:18000/
    """
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
