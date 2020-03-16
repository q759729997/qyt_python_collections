# docker_test镜像
FROM docker.io/python:3.6-buster

# 执行安装命令
# 分步骤执行
# RUN pip install jieba -i https://pypi.douban.com/simple
# RUN pip install pandas -i https://pypi.douban.com/simple
# 合并命令，减少docker层
RUN pip install jieba -i https://pypi.douban.com/simple && \
    pip install pandas -i https://pypi.douban.com/simple && \
    # 清理pip安装缓存；镜像大小由1.16GB变为1.09GB
    rm -rf /root/.cache/*

CMD ["python", "--version"]
# 构建镜像：docker build -f docker_test.dockerfile -t docker_test .
# 删除镜像：docker rmi -f docker_test
# 查看镜像安装历史：docker history docker_test
# 导出镜像：docker save -o docker_test.tar docker_test
# 压缩镜像：tar -czvf docker_test.tar.gz docker_test.tar
# 解压镜像：tar -xzvf docker_test.tar.gz
# 导入镜像：docker load -i docker_test.tar