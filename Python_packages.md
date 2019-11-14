# Python常用安装包与规范

## 代码风格检查与格式化

- 安装包

~~~
pip install flake8 -i https://pypi.douban.com/simple  # 代码检查工具
pip install yapf -i https://pypi.douban.com/simple  # Google开源的Python格式化工具
~~~

- 代码规范：<https://www.runoob.com/w3cnote/google-python-styleguide.html>
- 一行代码过长时的处理

	- 括号内的参数很多的时候, 为了满足每一行的字符不超过79个字符, 
	- 需要将参数换行编写, 这个时候换行的参数应该与上一行的括号对齐.
	- 或者将所有参数换行编写, 此时第一行不能有参数, 
	- 即第一行的最后一个字符一定要是(, 换行后需要有一个缩进. 
	- 类似的规则也用在[], {}上.
