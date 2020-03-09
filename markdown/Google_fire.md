# fire使用说明

## 简介

- Python Fire是一个Python库，只需对Fire进行一次调用即可将任何Python组件转变为命令行界面。
- 参考手册：<https://blog.csdn.net/taolusi/article/details/81046019>
- github地址：<https://github.com/google/python-fire>

## 终端命令，输入参数数据类型

~~~python
$ python example.py 10
int
$ python example.py 10.0
float
$ python example.py hello
str
$ python example.py '(1,2)'
tuple
$ python example.py [1,2]
list
$ python example.py True
bool
$ python example.py {name: David}
dict
~~~