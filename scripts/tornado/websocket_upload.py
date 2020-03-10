"""
Socket Tornado
参考资料：https://blog.csdn.net/qq_33961117/article/details/94624357
在线websocket测试：http://ws.douqq.com/
在线图像转流：https://tu.sioe.cn/gj/tupian-shujuliu/
"""
import re
import json
import traceback
import codecs
import base64

import tornado.ioloop
from tornado.websocket import WebSocketHandler

from tornado.options import define, options
define("port", default=18000, help="run on the given port", type=int)


class IndexHandler(WebSocketHandler):

    def open(self, *args, **kwargs):
        print("WebSocket opened")

    def on_message(self, message):
        """处理client发送的消息"""
        print('message:{}'.format(message[:20]))
        response_data = {'success': False, 'Object': None}
        try:
            req_data = json.loads(message)
            image = req_data.get('image', None)
            print('image:{}'.format(image[:20]))
            if image.startswith('data:image'):
                file_name = './temp/socket.jpg'
                # 图片解码保存
                result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", image, re.DOTALL)
                if result:
                    data = result.groupdict().get("data")
                    with codecs.open(file_name, "wb") as fw:
                        fw.write(base64.urlsafe_b64decode(data))
                else:
                    raise Exception("image error")
            else:
                file_name = './temp/socket.txt'
                with codecs.open(file_name, mode='w', encoding='utf8') as fw:
                    fw.write(image)
            response_data['success'] = True
            response_data['Object'] = file_name
        except Exception as e:
            traceback.print_exc()
            response_data['success'] = False
            response_data['Object'] = 'request error : ' + str(e)
        self.write_message(response_data)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        """允许跨域通讯问题"""
        return True


if __name__ == "__main__":
    """
    访问链接：
    ws://127.0.0.1:18000/
    {"image":"数据"}
    """
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
