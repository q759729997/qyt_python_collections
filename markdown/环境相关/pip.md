# pip命令

- 安装包

~~~shell
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
pip search SomePackage  # 搜索包
~~~

- 升级包

~~~shell
pip install --upgrade SomePackage
pip install --upgrade  -i https://pypi.douban.com/simple/ jieba
~~~

- 卸载包：

~~~shell
pip uninstall SomePackage
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

- 依赖文件添加至pip包，项目根目录下创建文件`MANIFEST.in`

~~~
# This actually adds the data file.
# basic
include requirements.txt
include README.md
include LICENSE
# others
include kdTimeConvert/models/modelfiles/holi_solar.json
~~~
