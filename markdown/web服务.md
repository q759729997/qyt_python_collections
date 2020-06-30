# 前后端交互

## 跨域问题

- 测试网站：http://www.runoob.com/try/try.php?filename=tryjquery_ajax_post
- 修改请求体，点击按钮，查看是否请求成功

~~~
$.post("xx",{
			question:"99式主战坦克有多高"
		}
~~~

### flask跨域问题方案

- 方案1

~~~
pip install flask_cors

from flask_cors import CORS
server = Flask(__name__)
CORS(server, supports_credentials=True)
~~~

- 方案2

~~~
server = Flask(__name__)
@server.after_request
def after_request(response):
   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
   # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response
~~~

## WSGI

- [Python uWSGI 安装配置](https://www.runoob.com/python3/python-uwsgi.html)
- WSGI的全称是Web Server Gateway Interface，翻译过来就是Web服务器网关接口。具体的来说，WSGI是一个规范，定义了Web服务器如何与Python应用程序进行交互，使得使用Python写的Web应用程序可以和Web服务器对接起来。
- 添加并发和监控，生成 4 个进程, 每个进程有 2 个线程。如果你要执行监控任务，可以使用 stats 子系统，监控的数据格式是 JSON

~~~shell
uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
~~~

### WSGI存在的目的有两个：

- 让Web服务器知道如何调用Python应用程序，并且把用户的请求告诉应用程序。
- 让Python应用程序知道用户的具体请求是什么，以及如何返回结果给Web服务器。
