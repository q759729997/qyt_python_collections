import time
import stomp


class MyListener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


if __name__ == "__main__":
    """连接测试，参考资料：https://pypi.org/project/stomp.py/
    参考资料：https://www.cnblogs.com/andylhc/p/9337945.html
    访问链接：http://192.175.1.11:8161/admin
    """
    # 通过调用stomp下的Connection10方法，创建连接，指定ip和端口
    conn = stomp.Connection10([('192.175.1.11', 61612)])
    conn.set_listener('MyListener', MyListener())
    conn.connect(username="admin", passcode="admin", wait=True)
    conn.subscribe(destination='/queue/abcde', id=1, ack='auto')
    # conn.send(body='hello world！', destination='/queue/chatbot_send')
    time.sleep(10)
    conn.disconnect()
