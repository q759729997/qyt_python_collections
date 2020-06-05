from docx import Document
from docx import CorePropertiesPart


if __name__ == "__main__":
    """docx基本信息"""
    docx_file_name = './temp/1. 冀北电网调度控制管理规程（发文版）.docx'
    document = Document(docx_file_name)
    print(document.author)
