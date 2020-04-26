import time
import stomp


class MyListener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


if __name__ == "__main__":
    """连接测试，参考资料：https://www.cnblogs.com/traditional/p/11144123.html
    """
    # 通过调用stomp下的Connection10方法，创建连接，指定ip和端口
    conn = stomp.Connection10([('39.104.161.233', 61613)])
    conn.set_listener('MyListener', MyListener())
    conn.connect(username="admin", passcode="admin", wait=True)
    conn.subscribe(destination='/queue/test', id=1, ack='auto')
    conn.send(body='hello world！', destination='/queue/test')
    time.sleep(2)
    conn.disconnect()
