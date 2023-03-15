from typing import List, Tuple, Dict, Set

def get_one_dim_sum(l: List):
    l_out = None
    # 请在下一行编写代码, l是列表，需要返回列表中所有元素的和
    # 例如l=[1,2,3],则返回6

    return l_out

def element_wise_mul_one_dim(l0: List, l1:List):
    l_out = None
    # 请在下一行编写代码, l0 l1是列表，需要返回两个列表中逐位相乘的列表; 若不能相乘，则返回None
    # 例如l0=[1,2,3] l1=[4, 5, 6], 则要返回[1*4, 2*5, 3*6]
    # 例如l0=[1,2 ] l1=[4, 5, 6], 则要返回None

    return l_out

def get_two_dim_list_len(l: List[List]):
    l_out = None
    # 请在下一行编写代码, l是列表的列表，需要返回l中每个列表的长度，变成一个长度列表，例如[[1],[],[1,2]]需要返回[1,0,2]

    return l_out

def update_two_dim_list(l: List[List]):
    l_out = None
    # 请在下一行编写代码, l是列表的列表，删除l中空列表后返回，例如[[1],[],[1,2]]需要返回[[1], [1,2]]

    return l_out


def get_shape_two_dim_list(l: List[List]):
    l_out = None
    # 请在下一行编写代码, l是列表的列表，获得其形状列表；若不符合统一形状的情况，则返回None
    # 例如l=[[1, 3, 4], [3, 4, 5]]  需要返回[2, 3]
    # 例如l=[[1, 3], [3, 4, 5]]  需要返回None

    return l_out

def element_wise_add_two_dim_list(l0: List[List], l1: List[List]):
    l_out = None
    # 请在下一行编写代码, l0 l1是列表的列表，将两个列表逐位相加；若两个列表形状不一致或不符合相加条件，则返回None
    # 例如l0=[[1,2], [3,4]] l1=[[5,6], [7,8]] 需要返回[[5, 8], [10, 12]]
    # 例如l0=[[1], [3,4]] l1=[[5,6], [7,8]] 需要返回None
    # 例如l0=[[1, 3, 4], [3, 4, 5]] l1=[[5,6], [7,8]] 需要返回None

    return l_out

def transpose_two_dim_list(l: List[List]):
    l_out = None
    # 请在下一行编写代码, l是列表的列表，将列表转置；若列表形状不符合转置条件，则返回None
    # 例如[[1,2], [3,4]] 需要返回[[1, 3], [2, 4]]; [[1], [3,4]], 返回None

    return l_out

def multiply_two_dim_list(l0: List[List], l1: List[List]):
    l_out = None
    # 请在下一行编写代码, l0 l1是列表的列表，将l0 l1做以下运算
    # 例如l0=[[1,2], [3,4]] l1=[[5,6], [7,8]] 则返回 [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]]
    # 例如l0=[[1], [4]] l1=[[5],[6]] 则返回 [[1*5, 1*6], [4*5, 4*6]]
    # 例如l0的形状为[a, b]， l1形状为[c, d]，若不满足 a=d且b=c，则返回None

    return l_out


if __name__ == "__main__":
    ret = get_two_dim_list_len()