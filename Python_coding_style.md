# Python代码风格检查与格式化

## 参考资料

- `Google`代码规范：<https://www.runoob.com/w3cnote/google-python-styleguide.html>

## 依赖包安装

~~~python
pip install flake8 -i https://pypi.douban.com/simple  # 代码检查工具
pip install yapf -i https://pypi.douban.com/simple  # Google开源的Python格式化工具
~~~

## 常用规则

- 代码头部：程序的`main`文件应该以`#!/usr/bin/python2`或者`#!/usr/bin/python3`开始。`#!`先用于帮助内核找到`Python`解释器, 但是在导入模块时, 将会被忽略. 因此只有被直接执行的文件中才有必要加入`#!`.
- 一行代码过长时的处理

	- 括号内的参数很多的时候, 为了满足每一行的字符不超过79个字符, 
	- 需要将参数换行编写, 这个时候换行的参数应该与上一行的括号对齐.
	- 或者将所有参数换行编写, 此时第一行不能有参数, 
	- 即第一行的最后一个字符一定要是(, 换行后需要有一个缩进. 
	- 类似的规则也用在[], {}上.

## 命名规则

- 应避免的命名

~~~python
单字符名称, 除了计数器和迭代器.
包/模块名中的连字符(-)
双下划线开头并结尾的名称(Python保留, 例如__init__)
~~~

- 命名约定

~~~python
所谓"内部(Internal)"表示仅模块内可用, 或者, 在类内是保护或私有的.
用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
用双下划线(__)开头的实例变量或方法表示类内私有.
将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.
~~~

- Python之父Guido推荐的规范

| Type                       | Public             | Internal                                                     |
| :------------------------- | :----------------- | :----------------------------------------------------------- |
| Modules                    | lower_with_under   | _lower_with_under                                            |
| Packages                   | lower_with_under   | -                                                            |
| Classes                    | CapWords           | _CapWords                                                    |
| Exceptions                 | CapWords           | -                                                            |
| Functions                  | lower_with_under() | _lower_with_under()                                          |
| Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER                                             |
| Global/Class Variables     | lower_with_under   | _lower_with_under                                            |
| Instance Variables         | lower_with_under   | _lower_with_under (protected) or __lower_with_under (private) |
| Method Names               | lower_with_under() | _lower_with_under() (protected) or __lower_with_under() (private) |
| Function/Method Parameters | lower_with_under   | -                                                            |
| Local Variables            | lower_with_under   | -                                                            |

## 导入格式

- 每个导入应该独占一行
- 导入总应该放在文件顶部, 位于模块注释和文档字符串之后, 模块全局变量和常量之前. 导入应该按照从最通用到最不通用的顺序分组:

~~~python
标准库导入
第三方库导入
应用程序指定导入
~~~

- 每种分组中, 应该根据每个模块的完整包路径按字典序排序, 忽略大小写

~~~
import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar
~~~


## 函数定义

- 文档字符串应该包含函数做什么, 以及输入和输出的详细描述. 通常, 不应该描述"怎么做", 除非是一些复杂的算法. 文档字符串应该提供足够的信息, 当别人编写代码调用该函数时, 他不需要看一行代码, 只要看文档字符串就可以了. 对于复杂的代码, 在代码旁边加注释会比使用文档字符串更有意义.
- 函数和方法注释说明。如果一个函数接受`*foo`(可变长度参数列表)或者`**bar` (任意关键字参数), 应该详细列出`*foo`和`**bar`
- 规则：

~~~python
Args:
列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.如果描述太长超过了单行80字符,使用2或者4个空格的悬挂缩进(与文件其他部分保持一致). 描述应该包括所需的类型和含义. 如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键字参数), 应该详细列出*foo和**bar.
Returns: (或者 Yields: 用于生成器)
描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略.
Raises:
列出与接口有关的所有异常.
~~~

- 示例：

~~~python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
~~~

## 类定义

- 类应该在其定义下有一个用于描述该类的文档字符串. 如果你的类有公共属性`(Attributes)`, 那么文档中应该有一个属性`(Attributes)`段. 并且应该遵守和函数参数相同的格式.

~~~python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
~~~

- 如果一个类不继承自其它类, 就显式的从`object`继承

~~~python
class SampleClass(object):
    pass
~~~

- 如果访问更复杂, 或者变量的访问开销很显著, 那么你应该使用像 `get_foo()` 和 `set_foo()` 这样的函数调用. 如果之前的代码行为允许通过属性`(property)`访问 , 那么就不要将新的访问函数与属性绑定. 这样, 任何试图通过老方法访问变量的代码就没法运行, 使用者也就会意识到复杂性发生了变化.

## 注释

- TODO：TODO注释应该在所有开头处包含"TODO"字符串, 紧跟着是用括号括起来的你的名字, email地址或其它标识符. 然后是一个可选的冒号. 接着必须有一行注释, 解释要做什么. 

~~~python
# TODO(kl@gmail.com): Use a "*" here for string repetition.
# TODO(Zeke) Change this to use relations.
~~~
