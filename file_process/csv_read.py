import codecs
import csv


def read_csv_texts(file_name):
    """读取csv文件，DictReader"""
    with codecs.open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        texts = list()
        for row in reader:
            content = str(row['content']).strip()
            if len(content) > 0:
                texts.append(content)
        return texts


if __name__ == "__main__":
    yue_news_file = 'data/yule_head_10.csv'
    # 读取csv文件，DictReader
    texts = read_csv_texts(yue_news_file)
    print('texts len：{}'.format(len(texts)))
    print('texts head 1：{}'.format(texts[0]))
