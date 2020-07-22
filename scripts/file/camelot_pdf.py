import camelot

tables = camelot.read_pdf('./temp/pdf/缺陷定级-国网公司输变电一次设备缺陷分类标准.pdf')

tables.export('./temp/pdf/camelot.json', f='json', compress=False)
