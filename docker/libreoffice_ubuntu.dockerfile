# docker_test镜像
FROM docker.io/ubuntu:20.04

# 执行安装命令
# 合并命令，减少docker层
RUN apt-get update && \
    apt-get install libreoffice && \
    apt-get install libreoffice-l10n-zh-cn libreoffice-help-zh-cn && \
    rm -rf /root/.cache/*

CMD ["soffice", "--version"]
# 自行在容器内进行安装，然后commit；中文显示需要设置相应语言环境
# docker run --name ubuntu_libreoffice -it -v /root/temp:/temp libreoffice_ubuntu:20_04  /bin/bash
# 构建镜像：docker build -f libreoffice_ubuntu.dockerfile -t libreoffice_ubuntu .
# 删除镜像：docker rmi -f libreoffice_ubuntu
# 查看镜像安装历史：docker history libreoffice_ubuntu
# 导出镜像：docker save -o libreoffice_ubuntu.tar libreoffice_ubuntu
# 压缩镜像：tar -czvf libreoffice_ubuntu.tar.gz libreoffice_ubuntu.tar
# 解压镜像：tar -xzvf libreoffice_ubuntu.tar.gz
# 导入镜像：docker load -i libreoffice_ubuntu.tar