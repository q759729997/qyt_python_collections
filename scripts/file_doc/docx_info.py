from docx import Document


if __name__ == "__main__":
    """docx基本信息"""
    docx_file_name = './temp/1. 冀北电网调度控制管理规程（发文版）.docx'
    document = Document(docx_file_name)
    # core_properties
    core_properties = document.core_properties
    print(core_properties.author)  # An entity primarily responsible for making the content of the resource.
    print(core_properties.title)
    print(core_properties.version)
    print(core_properties.modified)  # 2020-05-09 01:55:00
    # sections
    # paragraphs
    # tables
