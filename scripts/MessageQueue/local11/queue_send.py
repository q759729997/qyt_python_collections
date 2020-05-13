import stomp
import time

if __name__ == "__main__":
    """发送消息至消息队列；auto_content_length设置发送类型为text"""
    # 通过调用stomp下的Connection10方法，创建连接，指定ip和端口
    conn = stomp.Connection10([("192.175.1.11", 61612)], auto_content_length=False)
    # 但是activemq是需要账号密码的，因此这里连接到指定用户上面
    conn.connect(username="admin", passcode="admin", wait=True)

    # 发送消息
    for i in range(3):
        print('send message:{}'.format(i))
        text = "11:16 测试消息：query: 第{}条~".format(i)
        # text = str(text.encode('gbk'), encoding='gbk')
        conn.send(body=text, destination='/topic/chatbot_test')   # topic queue  chatbot_receive chatbot_send chatbot_test
        time.sleep(1)

    # 断开连接
    conn.disconnect()
