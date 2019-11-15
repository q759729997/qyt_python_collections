# Python编码

## 参考资料

- 菜鸟教程：<https://www.runoob.com/python3/python3-tutorial.html>
- Python之禅(一些Python技巧)：<https://foofish.net/category/pythonji-zhu.html>

## 函数定义

- `*foo`(可变长度参数列表)：加了星号 * 的参数会以元组`(tuple)`的形式导入，存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。
- `**bar` (任意关键字参数)：加了两个星号`**`的参数会以字典的形式导入。
- 简单的匿名函数

~~~python
lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2
print ("相加后的值为 : ", sum( 10, 20 ))
~~~

## 类定义

- 继承自`object`是为了使属性`(properties)`正常工作, 并且这样可以保护你的代码, 使其不受`Python 3000`的一个特殊的潜在不兼容性影响. 这样做也定义了一些特殊的方法, 这些方法实现了对象的默认语义, 包括 
~~~
__new__, 
__init__, 
__delattr__, 
__getattribute__, 
__setattr__, 
__hash__, 
__repr__, 
__str__ .
~~~

# 代码测试

## PyUnit (unittest) 的用法

- 参考资料：<http://c.biancheng.net/view/2679.html>
- 单元测试类必须继承`unittest.TestCase`，该类中的测试方法需要满足如下要求：

	- 测试方法应该没有返回值。
	- 测试方法不应该有任何参数。
	- 测试方法应以test 开头。

- 示例代码：

~~~python
import unittest

from fk_math import *


class TestFkMath(unittest.TestCase):
    # 测试一元一次方程的求解
    def test_one_equation(self):
        # 断言该方程求解应该为-1.8
        self.assertEqual(one_equation(5 , 9) , -1.8)
        # 断言该方程求解应该为-2.5
        self.assertTrue(one_equation(4 , 10) == -2.5 , .00001)
        # 断言该方程求解应该为27/4
        self.assertTrue(one_equation(4 , -27) == 27 / 4)
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            one_equation(0 , 9)
~~~

- TestCase 中最常用的断言方法

| 断言方法                  | 检查条件             |
| ------------------------- | -------------------- |
| assertEqual(a, b)         | a == b               |
| assertNotEqual(a, b)      | a != b               |
| assertTrue(x)             | bool(x) is True      |
| assertFalse(x)            | bool(x) is False     |
| assertIs(a, b)            | a is b               |
| assertIsNot(a, b)         | a is not b           |
| assertIsNone(x)           | x is None            |
| assertIsNotNone(x)        | x is not None        |
| assertIn(a, b)            | a in b               |
| assertNotIn(a, b)         | a not in b           |
| assertlsInstance(a, b)    | isinstance(a, b)     |
| assertNotIsInstance(a, b) | not isinstance(a, b) |

## 运行PyUnit测试
 
- 在编写完测试用例之后，可以使用如下两种方式来运行它们：
- 通过代码调用测试用例。程序可以通过调用 `unittest.main()` 来运行当前源文件中的所有测试用例。例如，在上面的测试用例中增加如下代码：

~~~python
if __name__ == '__main__':
    unittest.main()
~~~

- 使用 'unittest' 模块运行测试用例。使用该模块的语法格式如下：

~~~python
python -m unittest 测试文件
~~~

- 测试结果：

~~~python
．：代表测试通过。
F：代表测试失败，F 代表 failure。
E：代表测试出错，E 代表 error。
s：代表跳过该测试，s 代表 skip。
~~~

# 命令行工具

- Google fire：<https://github.com/google/python-fire>