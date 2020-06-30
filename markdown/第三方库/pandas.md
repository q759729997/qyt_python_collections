# 文件读取

- Excel读取

~~~
# 需要选中表格内数据，将其复制到其他sheet页，即可正常读取；sheet_name配置为相应的sheet页码
file_name = '~/aa.xlsx'
df = pd.read_excel(file_name, sheet_name='Sheet1')
~~~

# 数据预处理

- 空数据处理

~~~
df = df.fillna('')
~~~

# 统计分析

- 数据集分组与排序

~~~
df.groupby(['label']).count()
df.groupby(['label']).count().sort_values('content',ascending=False)
~~~

- 采样

~~~
import random
random.sample([10, 20, 30, 40, 50], k=4)
~~~

# 排序统计

- 计数统计

~~~
from collections import defaultdict
count_dict = defaultdict(int)  # 初始化为 0
for i in range(len(df)):
    label = str(df.iloc[i]['profession']).strip()
    content = str(df.iloc[i]['content']).strip()
    content = re.sub(r'\t|\r|\n', ' ', content).strip()
    if len(label) == 0 or len(content) == 0:
        continue
    count_dict[label] += 1
~~~

- 排序后输出

~~~
label_list = sorted(count_dict.items(), key=lambda d: d[1], reverse=True)
for key_,value_ in label_list:
    print('{} : {}'.format(key_,value_))
~~~

