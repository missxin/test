import  os.path

def get_file_type(file_name):
    """
    根据文件的名称来判断文件的类型
    :param file_name:
    :return:
    """
    result = -1
    if not os.path.isfile(file_name):
        return result
    path_name, ext = os.path.splitext(file_name)
    ext = ext.lower()
    if ext in ('.png', '.jpg', '.gif', '.bmp'):
        result = 0
    elif ext in ('.doc', '.docx'):
        result = 1
    elif ext in ('.ppt', '.pptx'):
        result = 2
    elif ext in ('.xls', '.xlsx'):
        result = 3

    return result