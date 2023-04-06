import json
import os
from typing import List, Tuple, Dict, Set
from Levenshtein import distance

class AisDeployInterface():
    """
    人工智能系统推理引擎 python接口类 AisDeployInterface
    """

    def __init__(self, param_path: str):
        """
        初始化
        :param param_path: 参数文件路径
        """
        # 在下一行编写代码，
        # 如果param_path是路径，则使用json读取param_path文件，将结果赋值给self.param
        # 如果param_path是字符串，则使用json将param_path转换为dict，将结果赋值给self.param


    def __del__(self):
        """
        析构函数
        """
        # 在下一行编写代码，将self.param赋值为None


    def get_param(self) -> Dict:
        """
        获取参数
        :return: 参数
        """
        out_dict = dict()
        # 在下一行编写代码，将self.param返回

        return out_dict

    def get_param_str(self) -> str:
        """
        获取参数字符串
        :return: 参数字符串
        """
        out_str = ""
        # 在下一行编写代码，将self.param转换为字符串后返回

        return out_str
    def update_param(self, param: Dict):
        """
        更新参数
        :param param: 参数
        """

        # 在下一行编写代码，将param更新到self.param中



    def delete_key(self, key: str):
        """
        删除key
        :param key: key
        """
        # 在下一行编写代码，删除self.param中的key


    def cal_str_distance(self, str1: str, str2: str) -> float:
        """
        计算字符串距离
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 字符串距离
        """
        out = 0.0
        # 在下一行编写代码，计算str1和str2的距离
        # 返回值为距离, 距离越大，相似度越小
        # 返回值取值范围为[0, 1]，越接近0，相似度越大

        return out

    def process(self, input_data: Dict) -> Dict:
        """
        推理
        :param input_data: 输入数据
        :return: 输出数据
        """
        out_dict = dict()
        # 在下一行编写代码，将input_data中的key为"input"的value提取出来
        # 判断提取出来的value是否为str类型，如果不是str类型，将其转换为str类型
        # 判断str类型的value和self.param中的key是否相等有相似的key，如果有相似的key，将self.param中的value赋值给out_dict
        # 如果没有相似的key，将value赋值给out_dict

        return out_dict



