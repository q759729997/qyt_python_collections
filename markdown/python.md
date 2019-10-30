# 编码规范

- Python头

~~~
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
~~~

- Python编码支持：https://docs.python.org/3/library/codecs.html#standard-encodings

## 守护进程

~~~
nohup python ./train.py >> ./log_train.log 1>&1 &
~~~

# 其他

## 忽略warning

~~~
import warnings
warnings.filterwarnings('ignore')  # "error", "ignore", "always", "default", "module" or "once"
~~~

# 参数传入

- 定义

~~~
import argparse

def args(arg_parser):
    arg_parser.add_argument('-encoding', '--encoding', default='utf8', help='file encoding.')
    arg_parser.add_argument('-g', '--gold_file', help='gold data file input.')
    arg_parser.add_argument('-p', '--pred_file', help='predicted file input.')
    arg_parser.add_argument('task', choices=['cws', 'pos'], help='The module to be evaluate.')
    arg_parser.add_argument('model', choices=name_systems_map.keys(), help='The system to be used.')
~~~

- 使用

~~~
parser = argparse.ArgumentParser()
    args(parser)
    ags = parser.parse_args()
    file_gold = codecs.open(ags.gold_file, 'r', ags.encoding)
~~~

## 计数

~~~
line_index = 0
    line_count = len(file_paths)
    for temp_path in file_paths:
        cmd = 'chmod 777 {}'.format(temp_path)
        line_index += 1
        print('当前：{}，合计：{}'.format(line_index, line_count), end='\r')
        os.system(cmd)
~~~

