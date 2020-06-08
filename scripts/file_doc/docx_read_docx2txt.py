import codecs

import docx2txt


if __name__ == "__main__":
#     docx_file_name = './temp/42--2020冀北电网调度细则--古杨树启动细则修改（0427）v04--张南85万.docx'
#     output_file_name = './temp/42--2020冀北电网调度细则--古杨树启动细则修改（0427）v04--张南85万_docx2txt.txt'
    docx_file_name = './temp/1. 冀北电网调度控制管理规程（发文版）.docx'
    output_file_name = './temp/1. 冀北电网调度控制管理规程（发文版）_docx2txt.txt'
    text = docx2txt.process(docx_file_name)
    with codecs.open(output_file_name, mode='w', encoding='utf8') as fw:
        fw.write('{}\n'.format(text))
