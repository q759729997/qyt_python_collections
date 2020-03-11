# python36镜像
FROM docker.io/python:3.6-buster

# 修改sh权限
RUN pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip show torch

CMD ["python", "--version"]
# 构建镜像 docker build -f pytorch1_2.dockerfile -t pytorch1_2 .