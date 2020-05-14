import time
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import stomp  # noqa
print('stomp module path :{}'.format(stomp.__file__))  # 输出测试模块文件位置


if __name__ == "__main__":
    """发送消息至消息队列；auto_content_length设置发送类型为text"""
    # 通过调用stomp下的Connection10方法，创建连接，指定ip和端口
    conn = stomp.Connection10([("192.175.1.11", 61613)], auto_content_length=False)
    # 但是activemq是需要账号密码的，因此这里连接到指定用户上面
    conn.connect(username="admin", passcode="admin", wait=True)

    # 发送消息
    # message_type = 'queue'
    for i in range(3):
        print('send message:{}'.format(i))
        text = "ActiveMq Python 发送的消息: 第{}条~".format(i)
        # text = str(text.encode('gbk'), encoding='gbk')
        conn.send(body=text, destination='/queue/abcde')   # topic queue  chatbot_receive chatbot_send chatbot_test a_0514
        time.sleep(1)

    # 断开连接
    conn.disconnect()
