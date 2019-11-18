from fastNLP.io import WeiboSenti100kPipe
from fastNLP.embeddings import BertEmbedding
from fastNLP.io.pipe.qa import CMRC2018Loader
from fastNLP.io import CNXNLILoader
from fastNLP.io import WeiboNERLoader
from fastNLP.embeddings import StaticEmbedding
from fastNLP import Vocabulary


if __name__ == "__main__":
    # 下载情感分析-分类数据
    data_bundle = WeiboSenti100kPipe().process_from_file()
    data_bundle.rename_field('chars', 'words')
    # 下载bert
    embed = BertEmbedding(data_bundle.get_vocab('words'), model_dir_or_name='cn-wwm', include_cls_sep=True)
    # 问答数据
    data_bundle = CMRC2018Loader().load()
    # 文本匹配
    data_bundle = CNXNLILoader().load()
    # NER
    data_bundle = WeiboNERLoader().load()
    # embedding
    vocab = Vocabulary()
    vocab.add_word_lst("你 好 .".split())
    embed = StaticEmbedding(vocab, model_dir_or_name='cn-sgns-literature-word')
