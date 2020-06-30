# 常用模板

- 常用包引入

~~~
import re
import codecs
import json
import csv
import pandas as pd
~~~

- pandas 读取文件

~~~
file_name = '~/aa.csv'  # 文件名称
df = pd.read_csv(file_name)
df = df.fillna('')
df.head()
df.info()
~~~

- 数据读取

~~~
data_list = list()
for i in range(len(df)):
    word = str(df.iloc[i]['Unnamed: 0']).strip()
    if len(word) > 0:
        data_list.append(word)
print(len(data_list))
print(data_list[:5])
~~~

- txt输出

~~~
output_path = '~/aa.txt'
with codecs.open(output_path, mode='w', encoding='utf8') as fw:
    for line in data_list:
        fw.write('{}\n'.format(line))
~~~

# 安装配置

- 安装：

~~~
pip install notebook  # 安装
jupyter notebook  # 启动
~~~

- windows下修改默认路径：<http://note.youdao.com/noteshare?id=b0dad7bc188a474aede5795218d52377&sub=75FA24FFD99E48F986F68986A30BF7E7>

- 服务器上jupyter notebook设置远程访问：<https://blog.csdn.net/simple_the_best/article/details/77005400>