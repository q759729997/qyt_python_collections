# python36镜像
FROM docker.io/python:3.6-buster

# 修改sh权限
RUN pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip show torch

CMD ["python", "--version"]
# 构建镜像 docker build -f pytorch_1_2.dockerfile -t pytorch_1_2 .
# 导出镜像：docker save -o pytorch_1_2.tar pytorch_1_2
# 压缩镜像：tar -czvf python36.tar.gz pytorch_1_2.tar
# 解压镜像：tar -xzvf python36.tar.gz
# 导入镜像：docker load -i python36.tar