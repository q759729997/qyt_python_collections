#  日志输出

- 日志

~~~
# 日志初始化
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info('logging test')
~~~