import sys
sys.path.append(".")
from basic.ops import *

def test_get_list_len():
    ret = get_list_len([1,2])
    assert ret == 2

def test_get_list_append_1():
    ret = get_list_append_1([1,2])
    assert ret == [1,2,1]

def test_get_list_reverse():
    ret = get_list_reverse([1, 2, 3, 4])
    assert ret == [4, 3, 2, 1]
    ret = get_list_reverse([1, 2])
    assert ret == [2, 1]

def test_get_list_exists():
    ret = get_list_exists([1, 2, 3], 1)
    assert ret == True
    ret = get_list_exists([1, 2, 3], 4)
    assert ret == False