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
- [pdftabextract：从扫描的文档中释放表格数据](https://datascience.blog.wzb.eu/2017/02/16/data-mining-ocr-pdfs-using-pdftabextract-to-liberate-tabular-data-from-scanned-documents/)
- [Parse text, table and layout from PDF file with PyMuPDF](https://github.com/dothinking/pdf2docx)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/module.html)
~~~shell
http://coolwanglu.github.io/pdf2htmlEX/doc/tb108wang.html
alias pdf2htmlEX="docker run -ti --rm -v ~/pdf:/pdf bwits/pdf2htmlex pdf2htmlEX"
pdf2htmlEX -h 
pdf2htmlEX --zoom 1.3 test.pdf
~~~

### ocrPDF

- [ocrmypdf,效果很一般](https://ocrmypdf.readthedocs.io/en/latest/languages.html)

~~~shell
docker cp /root/qiaoyongtian/temp/image.pdf ubuntu_zh_java_1_8_0:/root/   
ocrmypdf -l chi_sim image.pdf image_searchable.pdf
root@f541d06e944d:/# ocrmypdf --version
9.6.0+dfsg
tesseract --list-langs
# Display a list of all Tesseract language packs
apt-cache search tesseract-ocr
# Install Chinese Simplified language pack
apt-get install tesseract-ocr-chi-sim
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
