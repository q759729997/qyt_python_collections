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