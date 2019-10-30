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

