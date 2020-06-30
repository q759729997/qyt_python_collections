# pip配置

- Linux下pip配置

~~~
mkdir ~/.pip
cd ~/.pip/
vim pip.conf
~~~

~~~
[global]
index-url=http://pypi.douban.com/simple
[install]
trusted-host =
    pypi.douban.com
~~~

# conda安装

- 清华源：[https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda]

## Linux系统

~~~
cd /data/home/<your_user_name>
mkdir miniconda3  具体路径根据自己实际情况进行选择，请在自己目录下面进行相关操作。
cd miniconda3
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
安装bzip2
sh Miniconda3-latest-Linux-x86_64.sh
~~~

~~~
安装完毕后，source ~/.bashrc
执行下面命令检查是否安装成功：conda list
~~~

## 环境管理

- 创建环境

~~~
conda create --name python36 python=3.6
~~~

- 进入环境

~~~
source activate python36
~~~

- 退出环境

~~~
source deactivate python27
~~~

- 删除环境

~~~
conda env list
conda env remove -n env_name
~~~

- 导入环境

~~~
# miniconda3/envs
conda create -n cetc --clone /data/share/conda_env/cetc
~~~

## 包安装

~~~
pip freeze --local | grep -v '^-e' | cut -d = -f 1  | xargs -n1 pip install -U  # 升级所有包
~/.cache/pip # 缓存位置
~~~

## 包删除

- 包位置

~~~
~/miniconda3/envs/python36/lib/python3.6/site-packages
~~~