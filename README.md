# python开发常用

## conda

- jupyter

~~~python
jupyter notebook --allow-root //启动,allow-root为root用户访问时需要添加的命令
pip install notebook -i https://pypi.douban.com/simple/ //安装
pip uninstall notebook  //卸载
jupyter notebook --generate-config //生成配置
pip install pyrsistent==0.15.0  //windows安装
~~~

- jupyter配置，以下设置可以保证远程访问服务器上的jupyter,xshell工具可以通过隧道设置端口转发，本地就可以使用localhost进行访问

~~~python
c.NotebookApp.ip = '*'  # ip配置，防止Cannot assign requested address
c.NotebookApp.port = 8765  # port配置
c.NotebookApp.notebook_dir = '/root/notebook'  # 默认启动路径
c.NotebookApp.open_browser = False  # 是否打开浏览器
~~~

- 安装Python包，包搜索地址： <https://pypi.org/project/pyrsistent/>

~~~python
pip install -U jieba -i https://pypi.douban.com/simple/  # 安装或更新
conda upgrade --all  # 更新所有包
python setup.py install  # 使用源码安装
~~~

- 环境相关

~~~python
source activate python36 或  conda activate python36 # 进入环境，Linux需加source
source deactivate 或  conda deactivate # 退出环境，Linux需加source
conda info  # 查看基本环境信息，包括Python版本号，运行环境等等
conda env list  # 查看所有环境
conda create --name python36 python=3.6  # 创建环境，并指明python版本
conda env remove -n python36 --all  # 删除环境，python36为环境名称，--all为删除该环境下所有包
conda create -n myenv --clone /data/conda_env  # 导入环境
/miniconda3/envs/python36/lib/python3.6/site-packages # 包位置
~~~

- 安装conda

~~~python
mkdir software  # 具体路径根据自己实际情况进行选择，请在自己目录下面进行相关操作。
cd software
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
安装 bzip2  # 例如 apt-get install bzip2
sh Miniconda3-latest-Linux-x86_64.sh  # 安装conda
source ~/.bashrc  # 安装完毕后,使环境变量生效
conda env list  # 执行此命令检查是否安装成功
~~~

- 设置pip源

~~~python
mkdir ~/.pip
cd ~/.pip/
vim pip.conf
# 以下为设置内容
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=http://mirrors.aliyun.com/pypi/simple/
~~~

- pip源列表

~~~python
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
豆瓣：http://pypi.douban.com/simple/
~~~

## 模型训练

- 显卡查看

~~~python
nvidia-smi  # 查看显卡占用
~~~

- torch安装

~~~python
pip install torch torchvision  # 带有cuda的参照官网https://pytorch.org/
~~~

## 进程守护

- tmux

~~~python
tmux new -s python36 会话名   //新起一个会话
tmux ls  //查看现有的会话
tmux a  //进入最近的会话
tmux a -t  会话名 //进入指定会话
tmux kill-session -t 会话名 //干掉指定会话
tmux detach //离开会话
~~~

## Ubuntu

- 安装

~~~python
apt install tmux # 安装软件
apt update  # apt更新
~~~
