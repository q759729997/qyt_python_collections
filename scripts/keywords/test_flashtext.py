"""
关键词抽取：

Extract Keywords from sentence or Replace keywords in sentences.
github链接： https://github.com/vi3k6i5/flashtext
依赖安装： pip install flashtext
"""
from flashtext import KeywordProcessor


if __name__ == "__main__":
    keywords = [
        '北京',
        '天安门',
        '北京天安门',
        # '爱北'
    ]
    # 加入爱北后：[('爱北', 1, 3), ('天安门', 4, 7)]
    keyword_processor = KeywordProcessor()
    for word in keywords:
        keyword_processor.add_keyword(word)
    keywords_found = keyword_processor.extract_keywords('我爱北京天安门。')
    print(keywords_found)
    # ['北京天安门']
    keywords_found = keyword_processor.extract_keywords('我爱北京天安门。', span_info=True)
    print(keywords_found)
    # [('北京天安门', 2, 7)]  只返回最长词串
