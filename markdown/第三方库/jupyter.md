# jupyter notebook手册

## 魔法命令

- 参考：[数据分析](https://blog.csdn.net/weixin_41504611/article/details/103465972)
- 魔法命令分为%与%%两种形式，即在相应的命令前使用%或%%前缀。但并非所有的魔法命令都支持这两种形式。

~~~wiki
% 行模式
%% 单元格模式
~~~

### writefile（file）

- 格式： %%writefile [-a] filename
- 将单元格的内容写入到文件中。如果文件不存在则创建，如果文件存在，则覆盖文件。如果指定-a选项，则追加内容（不覆盖）。writefile以前命名为file，为了兼容，file命令依然还能够使用。

~~~shell
%%writefile example_submissions/submission/submission.py

from .agents import MyAgent
from grid2op.Reward import ConstantReward

def make_agent(env, submission_dir):
    """
    This function will be used by codalab to create your agent. It should accept exactly an environment and a path
    to your submission directory and return a valid agent.
    """
    agent = MyAgent(env.action_space)
    return agent

# reward must be a subclass of grid2op.Reward.BaseReward.BaseReward:
reward = ConstantReward # you can also create your own reward class
~~~

## 常用模板

- 常用包引入

~~~shell
import re
import codecs
import json
import csv
import pandas as pd
~~~

- pandas 读取文件

~~~shell
file_name = '~/aa.csv'  # 文件名称
df = pd.read_csv(file_name)
df = df.fillna('')
df.head()
df.info()
~~~

- 数据读取

~~~shell
data_list = list()
for i in range(len(df)):
    word = str(df.iloc[i]['Unnamed: 0']).strip()
    if len(word) > 0:
        data_list.append(word)
print(len(data_list))
print(data_list[:5])
~~~

- txt输出

~~~shell
output_path = '~/aa.txt'
with codecs.open(output_path, mode='w', encoding='utf8') as fw:
    for line in data_list:
        fw.write('{}\n'.format(line))
~~~

## 安装配置

- 安装：

~~~shell
pip install notebook  # 安装
jupyter notebook  # 启动
~~~

- windows下修改默认路径：<http://note.youdao.com/noteshare?id=b0dad7bc188a474aede5795218d52377&sub=75FA24FFD99E48F986F68986A30BF7E7>
- 服务器上jupyter notebook设置远程访问：<https://blog.csdn.net/simple_the_best/article/details/77005400>
