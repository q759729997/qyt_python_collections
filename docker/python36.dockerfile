# python36镜像
FROM docker.io/python:3.6-buster

CMD ["python", "--version"]
# 构建镜像 docker build -f python36.dockerfile -t python36 .
# 导出镜像：docker save -o python36.tar python36
# 压缩镜像：tar -czvf python36.tar.gz python36.tar
# 解压镜像：tar -xzvf python36.tar.gz
# 导入镜像：docker load -i python36.tar