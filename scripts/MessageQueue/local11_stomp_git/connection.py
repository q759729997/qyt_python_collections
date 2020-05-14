import time
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import stomp  # noqa
print('stomp module path :{}'.format(stomp.__file__))  # 输出测试模块文件位置


def connect_and_subscribe(conn):
    conn.connect('admin', 'admin', wait=True)
    conn.subscribe(destination='/queue/abcde', id=1, ack='auto')


class MyPrintingListener(stomp.PrintingListener):
    """打印日志的Listener"""
    def __init__(self, conn, print_to_log=False):
        self.conn = conn
        self.print_to_log = print_to_log

    # def on_error(self, headers, message):
    #     print('received an error "%s"' % message)

    # def on_message(self, headers, message):
    #     print('received a message "%s"' % message)
    #     for x in range(10):
    #         print(x)
    #         time.sleep(1)
    #     print('processed message')

    def on_disconnected(self):
        print('disconnected')
        connect_and_subscribe(self.conn)


if __name__ == "__main__":
    conn = stomp.Connection10([("192.175.1.11", 61613)], auto_content_length=False)
    conn.set_listener('', MyPrintingListener(conn))
    connect_and_subscribe(conn)
    for i in range(100):
        print('sleep:{}'.format(i))
        time.sleep(1)
    conn.disconnect()
