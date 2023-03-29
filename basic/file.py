import json
from typing import List, Tuple, Dict, Set

def read_txt_file(path: str):
    l_out = None
    # 请在下一行编写代码, path是txt文件的路径，要求以读打开该文件，若打开失败则返回空列表
    # 打开成功后逐行读取，将每一行的换行符去掉后，作为一个元素加入到列表中并输出

    return l_out

def write_txt_file(path: str, ls:List):
    # 请在下一行编写代码, path是txt文件的输出路径，请将ls中元素逐行写入path路径的文件中

    return None

def read_json_file(path: str):
    out = None
    # 请在下一行编写代码, path是json文件的路径，要求以读打开该文件，若打开失败则返回None
    # 打开成功后读取json文件，将结果编码成str返回

    return out

def write_json_file(path: str, ds:List[Dict]):
    # 请在下一行编写代码, path是json文件的输出路径，请将ds的list中每个元素的name字段删除后，将json输出到文件中
    # 例如[{"name":"1", "x":1},{"name":2, "x":2}] 则需要将[{"x":1},{"x":2}]输出

    return None

def read_xml_file(path: str):
    out = None
    import xmltodict
    # 请在下一行编写代码, path是xml文件的路径，要求以读打开该文件，若打开失败则返回None
    # 打开成功后读取xml文件，将结果编码成str返回


    return out

def write_xml_file(path: str, ds:List[Dict]):
    import dicttoxml
    # 请在下一行编写代码, path是xml文件的输出路径，请将ds的list中每个元素的name字段删除后，使用dicttoxml库将xml输出到文件中
    # 根节点为root, 且不使用属性
    # 例如[{"name":"1", "x":1},{"name":2, "x":2}] 则需要将[{"x":1},{"x":2}]输出为
    # {'root': {'item': [{'name': '1', 'value': '2'}, {'name': '2', 'value': '3'}]}}


    return None

def read_csv_file(path: str):
    out = None
    import csv
    # 请在下一行编写代码, path是csv文件的路径，要求以读打开该文件，若打开失败则返回None
    # 打开成功后读取csv文件，将每行的结果使用空格分割后，作为一个元素加入到列表中
    # 例如[["1 2 3"],["4 5 6"]] 则需要将[['1', '2', '3'],['4', '5', '6']]输出




    return out