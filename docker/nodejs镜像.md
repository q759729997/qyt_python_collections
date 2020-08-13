# nodejs镜像

## 制作nodejs镜像

- 启动容器：

~~~shell
docker run -it --name ubuntu_zh_20_04 docker.io/q759729997/ubuntu_zh:20_04 /bin/bash
docker rm -f ubuntu_zh_20_04
~~~

- nodejs安装

~~~shell
[容器内执行]
apt-get install nodejs
apt-get install npm
# 查看安装版本
node -v
npm -l
~~~

- 提交镜像

~~~shell
[宿主机执行]
# 提交镜像
docker commit ubuntu_zh_20_04  ubuntu_zh_nodejs:10_19_0
# 打包镜像
docker save -o ubuntu_zh_nodejs_10_19_0.tar ubuntu_zh_nodejs:10_19_0
# 压缩镜像
tar -czvf ubuntu_zh_nodejs_10_19_0.tar.gz ubuntu_zh_nodejs_10_19_0.tar
~~~

## 镜像使用

### 首次启动时

- 使用镜像启动容器：

~~~shell
# -v /宿主机:/容器 --privileged  # 挂载
[宿主机执行]
docker run -it --name ubuntu_zh_nodejs_10_19_0 \
    -v /root/qiaoyongtian/projects:/root/ --privileged \
    ubuntu_zh_nodejs:10_19_0 /bin/bash  # 启动容器，并进入bash
[容器内执行]
node -v  # 验证node版本
npm -l
~~~

### docker容器操作常用

- 容器连接，进入bash操作界面

~~~shell
# 【继续运行docker run启动时的shell界面】
docker attach --sig-proxy=false ubuntu_zh_nodejs_10_19_0  # 连接到正在运行中的容器
# 【打开一个新的shell界面，但其对bash的支持不友好】
docker exec -it ubuntu_zh_nodejs_10_19_0 /bin/sh  # 在容器中开启一个交互模式的终端
# 退出且不关闭容器：Ctrl+P+Q
~~~

- 容器信息查看

~~~shell
docker top ubuntu_zh_nodejs_10_19_0  # 查看容器内的进程信息
docker inspect ubuntu_zh_nodejs_10_19_0  # 获取容器/镜像的元数据详细信息
docker logs ubuntu_zh_nodejs_10_19_0  # 获取容器的日志
docker port ubuntu_zh_nodejs_10_19_0  # 列出指定的容器的端口映射
~~~

- 容器启动与停止

~~~shell
docker start ubuntu_zh_nodejs_10_19_0  # 启动node容器
docker rm -f ubuntu_zh_nodejs_10_19_0  # 删除node容器
docker stop ubuntu_zh_nodejs_10_19_0  # 停止node容器
~~~

- 容器与宿主机之间拷贝文件

~~~shell
# 从宿主机到java容器
docker cp /root/qiaoyongtian/software/java/jdk-8u201-linux-x64.tar.gz ubuntu_zh_nodejs_10_19_0:/root/java/
# 从java容器到宿主机
docker cp ubuntu_zh_nodejs_10_19_0:/root/java/jdk-8u201-linux-x64.tar.gz /root/qiaoyongtian/software/java/
~~~