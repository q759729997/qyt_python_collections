import stomp
import time


class SampleListener(stomp.ConnectionListener):

    def on_message(self, headers, message):
        # headers是一个字典，里面很多内容，是一个字典，headers['destination']是对应的队列名称
        print(f"headers:{headers['destination']}, message:{message}")

    def on_error(self, headers, message):
        print(f"headers:{headers['destination']}, message:{message}")

    def on_disconnected(self):
        """
        Called by the STOMP connection when a TCP/IP connection to the
        STOMP server has been lost.  No messages should be sent via
        the connection until it has been reestablished.
        """
        print('on_disconnected')


if __name__ == "__main__":
    """接收消息队列中的消息"""
    # 通过调用stomp下的Connection10方法，创建连接，指定ip和端口
    conn = stomp.Connection10([("192.175.1.11", 61613)], auto_content_length=False)
    # 绑定监听器，我们这里只有一个，所以名字什么的无所谓
    conn.set_listener("", SampleListener())
    # 但是activemq是需要账号密码的，因此这里连接到指定用户上面
    conn.connect(username="admin", passcode="admin", wait=True)
    # 订阅到指定的队列，这个要和发送端发送的队列保持一致
    # 当发送端有消息过来时，消息的内容会自动传递到SampleListener类下的on_message的message参数里。headers则包含了一些额外信息，比如时间戳、队列名等等
    # 当然，如果有错误就会传到on_error中，不过这里没有定义，可以的话定义一下也是好的，参数和on_message是一样的
    conn.subscribe("/topic/chatbot_test")  # topic queue  chatbot_receive chatbot_send chatbot_test

    # 让程序不停下，不然程序立马就结束了
    print('启动监听')
    while True:
        pass
    print('结束监听')

    # 断开连接
    conn.disconnect()
