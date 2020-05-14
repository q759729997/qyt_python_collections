import stomp
import time

if __name__ == "__main__":
    """发送消息至消息队列"""
    # 通过调用stomp下的Connection10方法，创建连接，指定ip和端口
    conn = stomp.Connection10([("39.104.161.233", 61613)])
    # 但是activemq是需要账号密码的，因此这里连接到指定用户上面
    conn.connect(username="admin", passcode="admin", wait=True)

    # 发送消息
    for i in range(3):
        print('发送第{}条'.format(i))
        conn.send("/topic/test", "测试消息：query:{}".format(i))  # queue topic
        time.sleep(1)

    # 断开连接
    conn.disconnect()
