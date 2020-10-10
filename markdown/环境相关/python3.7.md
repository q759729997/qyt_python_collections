# python3.7

## Windows环境下python3.7出现ssl或者tsl不可用的解决方法

~~~shell
import _ssl             # if we can't import it, let the error propagate
ModuleNotFoundError: No module named '_ssl'
~~~

- 问题的可能原因是缺少openssl或者版本过低。
- 解决方法为到https://slproweb.com/products/Win32OpenSSL.html上下载winopessl，直接下载第一个MSI安装即可：

~~~wiki
Win64 OpenSSL v1.1.1g Light
EXE | MSI
~~~