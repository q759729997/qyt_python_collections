# pytorch_1_4_0镜像
FROM python36

# 拷贝文件
COPY ./torch-1.4.0+cpu-cp36-cp36m-linux_x86_64.whl /root/
# 执行安装命令
RUN pip install /root/torch-1.4.0+cpu-cp36-cp36m-linux_x86_64.whl && \
    # 清理pip安装缓存
    rm -rf /root/.cache/* && \
    rm -rf /root/torch-1.4.0+cpu-cp36-cp36m-linux_x86_64.whl

CMD ["python", "--version"]
# 构建镜像 docker build -f pytorch_1_4_0.dockerfile -t pytorch_1_4_0 .
# 删除镜像：docker rmi -f pytorch_1_4_0
# 导出镜像：docker save -o pytorch_1_4_0.tar pytorch_1_4_0
# 压缩镜像：tar -czvf pytorch_1_4_0.tar.gz pytorch_1_4_0.tar
# 解压镜像：tar -xzvf pytorch_1_4_0.tar.gz
# 导入镜像：docker load -i pytorch_1_4_0.tar