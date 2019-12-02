# json转码设置ensure_ascii

~~~
infobox = json.dumps(search_data.get('infobox', list()), ensure_ascii=False)
json.dumps(***, ensure_ascii=False)
~~~

# txt读写

- 读取txt

~~~
input_file = '~/train.txt'
data_list = list()
with codecs.open(input_file, mode='r', encoding='utf8') as fr:
    for line in fr:
        line = line.strip()
        if len(line) > 0:
            data_list.append(line)
    print('data_list len:{}'.format(len(data_list)))
    print('data_list:{}'.format(data_list[:2]))
~~~

- 输出txt

~~~
output_path = '~/aa.txt'
with codecs.open(output_path, mode='w', encoding='utf8') as fw:
    for line in data_list:
        fw.write('{}\n'.format(line))
~~~

# csv读写

- 读取csv

~~~
def get_processed_sents(file_name):
    """获取处理过的语句"""
    with codecs.open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        sents = list()
        for row in reader:
            sent = str(row['sent']).strip()
            if len(sent) > 0:
                sents.append(sent)
        return sents
~~~

- 输出csv文件

~~~
import csv
out_path = '~/aa.csv'
with codecs.open(out_path, 'w', encoding='utf-8') as csvout:
    writer = csv.writer(csvout)
    # 写入表头
    title_list = ('title', 'content')
    writer.writerow(title_list)
    for temp in news_list_v4:
        data_line = (temp[0], temp[1])
        writer.writerow(data_line)
~~~


# 文件夹读取

- 递归读取文件夹与文件

~~~
def listdir(path, file_names, file_paths):  # 传入存储的list
    """递归读取文件夹与文件"""
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            file_paths.append(file_path)
            listdir(file_path, file_names, file_paths)
        else:
            file_names.append(file_path)
~~~

- 递归读取文件

~~~
def get_file_names_recursion(path, file_names):
    """递归读取文件，file_names会递归更新.

    Args:
        path: 待递归检索的文件夹路径.
        file_names: 待输出结果的文件名列表.

    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            get_file_names_recursion(file_path, file_names)
        else:
            file_names.append(file_path)
~~~

