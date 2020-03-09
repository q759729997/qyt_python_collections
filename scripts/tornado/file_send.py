import codecs

import requests


if __name__ == "__main__":
    """文件发送
    http://2.python-requests.org/zh_CN/latest/user/quickstart.html
    """
    url = 'http://127.0.0.1:18000/upload'
    files = {'file': codecs.open('./data/yule_head_10.csv', mode='r', encoding='utf8')}
    r = requests.post(url, files=files)
    print(r.text)
