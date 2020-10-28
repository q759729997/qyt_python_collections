"""汇总文件大小"""
import os
import codecs

from tqdm import tqdm


def get_file_names_recursion(path, file_names):
    """ 递归读取输入路径下的所有文件，file_names会递归更新.

        @params:
            path - 待递归检索的文件夹路径.
            file_names - 待输出结果的文件名列表.

        @return:
            On success - 无返回值，文件输出至file_names中.
    """
    for file in os.listdir(path):
        try:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                get_file_names_recursion(file_path, file_names)
            else:
                file_names.append(file_path)
        except Exception:
            pass


if __name__ == "__main__":
    file_limit = 100 * 1024 * 1024  # MB
    root_path = 'E:/qyt'
    output_file = 'temp/big_file.txt'
    file_names = list()
    get_file_names_recursion(root_path, file_names)
    print('file_names len:{}'.format(len(file_names)))
    print('file_names example:{}'.format(file_names[:5]))
    with codecs.open(output_file, mode='w', encoding='utf8') as fw:
        for file_name in tqdm(file_names):
            try:
                file_size = os.path.getsize(file_name)
                if file_size > file_limit:
                    file_size = round(file_size/1024/1024, 3)
                    row_text = 'size: {} MB,  file: {}'.format(file_size, file_name)
                    fw.write(row_text + '\n')
            except Exception:
                pass
