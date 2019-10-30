# 编码

- python编码列表：[编码列表](https://docs.python.org/3/library/codecs.html#standard-encodings)

## 去掉连续空格

- 示例代码

~~~
import re
def remove_blank(text, keep=False):
    '''
    keep=False: 去除全部空格.
    keep=True: 去除连续的多个空格，保留一个.
    '''
    if keep is False:
        text = re.sub(r'\s+', '', text)
    else:
        text = re.sub(r'\s+', ' ', text)
    return text
~~~

- 返回结果

~~~
print(remove_blank('中    国      人', keep=True))
中 国 人
~~~

## 换句处理

~~~
if word in {'。', '！', '?', '……'}
~~~

