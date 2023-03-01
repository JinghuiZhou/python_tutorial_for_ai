import sys
sys.path.append(".")
from basic.variables import *

def test_get_variable_int():
    ret = get_variable_int()
    assert isinstance(ret, int)

def test_get_variable_float():
    ret = get_variable_float()
    assert isinstance(ret, float)

def test_get_variable_str():
    ret = get_variable_str()
    assert isinstance(ret, str)

def test_get_variable_list():
    ret = get_variable_list()
    assert isinstance(ret, list)

def test_get_variable_tuple():
    ret = get_variable_tuple()
    assert isinstance(ret, tuple)

def test_get_variable_set():
    ret = get_variable_set()
    assert isinstance(ret, set)

def test_get_variable_dict():
    ret = get_variable_dict()
    assert isinstance(ret, dict)

def test_op_add():
    ret = get_op_add(1, 2)
    assert ret == 3

def test_op_sub():
    ret = get_op_sub(2, 1)
    assert ret == 1

def test_op_div():
    ret = get_op_div(2, 3)
    assert ret == 2/3

def test_op_mod():
    ret = get_op_mod(17, 3)
    assert ret == 17%3

def test_get_str_slice():
    ret = get_str_slice("tzvtc", 1, 3)
    assert ret == "zv"

def test_get_str_duplicate():
    ret = get_str_duplicate("tzvtc")
    assert ret == "tzvtctzvtc"

def test_get_str_concat():
    ret = get_str_concat("tzvtc","ai")
    assert ret == "tzvtcai"

def test_get_list_slice():
    ret = get_list_slice([1,2,3,4], 1, 3)
    assert ret == [2, 3]

def test_get_list_slice_end():
    ret = get_list_slice_end([1,2,3,4])
    assert ret == [4]

def test_list_concat():
    ret = list_concat([1,2,3,4], [5])
    assert ret == [1,2,3,4,5]

def test_get_area():
    import math
    ret = get_area(4)
    assert ret == 16*math.pi