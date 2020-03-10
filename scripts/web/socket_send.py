import socket   # 客户端 发送一个数据，再接收一个数据


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
    client.connect(('localhost', 18000))  # 建立一个链接
    client.send('{"image":"数据"}'.encode(encoding='utf8'))
    data = client.recv(1024)  # 接收一个信息，并指定接收的大小 为1024字节
    print('recv:', data.decode())  # 输出我接收的信息
    client.close()  # 关闭这个链接
