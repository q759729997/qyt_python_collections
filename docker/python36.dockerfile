# python36镜像
FROM docker.io/python:3.6-buster

# 修改sh权限
RUN python --version

CMD ["python", "--version"]
# 构建镜像 docker build -f python36.dockerfile -t python36 .