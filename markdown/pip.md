# pip命令

~~~shell
pip install --upgrade  -i https://pypi.douban.com/simple/ jieba
~~~

## Python包操作

- 当前用户根目录下创建`.pypirc`，配置pypi信息

~~~shell
[distutils]
index-servers =
    pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: name
password: xxxx
~~~

- 打包上传

~~~shell
python setup.py sdist bdist_wheel  # 打包
twine upload dist/*.whl --verbose  # 将打包后的whl上传
# Linux下文件改为：manylinux2010
~~~
