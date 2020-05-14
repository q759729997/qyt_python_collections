# 11服务器消息队列测试

- 消息队列页面访问： <http://192.175.1.11:8161/admin>

## C语言发送消息

- 执行命令

~~~shell
cd /home/d5000/fujian/src/activemq/test/acmq_sender_test  # 脚本路径
vim main.cpp  # 修改配置，bool useTopics = true; std::string destURI = "chatbot_test"; a_0514
make  # 编译
cd /home/d5000/fujian/src/activemq/test/acmq_sender_test/linux  # 编译后，可执行文件路径

~~~
