## 数据库

- [tinydb，If you need a simple database with a clean API that just works without lots of configuration, TinyDB might be the right choice for you.](https://tinydb.readthedocs.io/en/latest/)

## 数据结构与算法

- [算法/数据结构/Python/剑指offer/机器学习/leetcode
](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython)

## 性能分析

- [Python性能分析](https://flystarhe.github.io/docs-2014/python/notes/profiler/#memory_profiler)
- 内存占用：[Monitor Memory usage of Python code](https://github.com/pythonprofilers/memory_profiler)

## PDF解析

- [extract tables from PDF](https://github.com/atlanhq/camelot)
- [Plumb a PDF for detailed information about each text character, rectangle, and line. Plus: Table extraction and visual debugging.](https://github.com/jsvine/pdfplumber)
- [PDFMiner is a text extraction tool for PDF documents.](https://github.com/euske/pdfminer)
- [pdf2HtmlEX Smallest pdf2htmlEX container and easiest way to convert pdf to html file (246MB)](https://hub.docker.com/r/bwits/pdf2htmlex)

~~~shell
alias pdf2htmlEX="docker run -ti --rm -v ~/pdf:/pdf bwits/pdf2htmlex pdf2htmlEX"
pdf2htmlEX -h 
pdf2htmlEX --zoom 1.3 test.pdf
~~~

## DOC解析

- [Mammoth .docx to HTML converter](https://github.com/mwilliamson/python-mammoth)
- [Pypandoc provides a thin wrapper for pandoc, a universal document converter.](https://github.com/bebraw/pypandoc)
- libreoffice[安装](https://www.jianshu.com/p/27749e454569)：

~~~shell
# 转换
soffice --invisible --headless --convert-to pdf 20200721.docx --outdir ./
soffice --invisible --headless --convert-to "html:HTML (StarWriter)":UTF8 ./11.doc --outdir ./
soffice --invisible --headless --convert-to "docx:MS Word 2007 XML":44,34,76 ./测试啊.doc --outdir ./
soffice --invisible --headless --convert-to "txt:Text (encoded):UTF8" ./测试啊.docx --outdir ./
# 卸载 yum erase libreoffice\*
yum install libreoffice-headless
yum -y install libreoffice-langpack-zh-Han*
# docker https://hub.docker.com/r/unifreq/libreoffice-headless
docker run -it -v /usr/share/fonts:/usr/share/fonts -v /usr/local/share/fonts:/usr/local/share/fonts -v /root/qiaoyongtian/temp:/tmp unifreq/libreoffice-headless --invisible --headless --convert-to html /tmp/张南85万.doc --outdir /tmp/html
# 乱码问题-把Windows下的字体C:\Windows\Fonts下的宋体，即simsun.ttc上传到linux服务器并赋值到上面的字体目录下赋予读写权限：https://www.bbsmax.com/A/ke5j2Va95r/
~~~

## CEB解析

- CEB是Chinese E-paper Basic的缩写，是北大方正电子公司拥有自主知识产权的一种版式文件格式，目前在我国政府机关公文处理中应用广泛。常用的字处理排版软件，如WORD、WPS等，生成的所有结果文件都可以方便地转换成CEB格式。

~~~wiki
方正ApabiReader 1.82版图书馆版支持虚拟打印
提取码:pgam
解压密码:www.duoluodeyu.com
~~~
