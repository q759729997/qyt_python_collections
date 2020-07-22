import codecs
import mammoth
from bs4 import BeautifulSoup

result = mammoth.convert_to_html("./temp/docx/风电AGC使用手册-序号丢失2.docx")
# soup = BeautifulSoup(result.value, 'html.parser')
# print(soup.prettify())
html_path = './temp/docx/风电AGC使用手册-序号丢失2.html'
with codecs.open(html_path, 'w', encoding='utf-8') as file:
    file.write(result.value)
