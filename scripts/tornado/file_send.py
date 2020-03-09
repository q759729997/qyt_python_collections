import codecs

import requests


if __name__ == "__main__":
    """文件发送
    http://2.python-requests.org/zh_CN/latest/user/quickstart.html
    """
    # json形式发送文件
    # url = 'http://127.0.0.1:18000/upload'
    # files = {'file': codecs.open('./data/yule_head_10.csv', mode='r', encoding='utf8')}
    # r = requests.post(url, files=files)
    # print(r.text)
    # 二进制流发送文件；https://tool.oschina.net/commons/
    url = "http://127.0.0.1:18000/upload_b"
    payload = codecs.open('./data/jay.jpg', mode='rb')
    headers = {
        'Content-Type': 'image/jpeg'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
