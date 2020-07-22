import codecs
import json
import pdfplumber

with codecs.open('./temp/pdf/pdfplumber.json', mode='w', encoding='utf8') as fw:
    with pdfplumber.open("./temp/pdf/缺陷定级-国网公司输变电一次设备缺陷分类标准.pdf") as pdf:
        for page in pdf.pages:
            fw.write('{}\n\n'.format(json.dumps(page.extract_table(), ensure_ascii=False)))
