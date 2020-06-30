# 说明

- 安装

~~~
pip install -U scikit-learn -i https://pypi.douban.com/simple/
~~~

# 数据处理

- 数据集划分

~~~
from sklearn.model_selection import train_test_split
train_data, val_data = train_test_split(data_list, test_size=0.2, shuffle=True)
val_data, test_data = train_test_split(val_data, test_size=0.5, shuffle=True)
print('数据切分结果： all:{}, train:{}, val:{}, test:{}'.format(len(data_list), len(train_data), len(val_data), len(test_data)))
~~~

