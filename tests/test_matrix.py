import sys
sys.path.append(".")
from basic.matrix import *

def test_get_one_dim_sum():
    ret = get_one_dim_sum([1, 3])
    assert  ret == 4
    ret = get_one_dim_sum([])
    assert  ret == 0

def test_element_wise_mul_one_dim():
    ret = element_wise_mul_one_dim([1, 3], [2, 4])
    assert ret == [2, 12]
    ret = element_wise_mul_one_dim([1, 1], [2, 4])
    assert ret == [2, 4]
    ret = element_wise_mul_one_dim([1], [2, 4])
    assert ret == None

def test_get_two_dim_list_len():
    ret = get_two_dim_list_len([[1],[],[1,2]])
    assert ret == [1,0,2]
    ret = get_two_dim_list_len([[1, 1],[],[1,2]])
    assert ret == [2,0,2]

def test_update_two_dim_list():
    ret = update_two_dim_list([[1],[],[1,2]])
    assert ret == [[1], [1,2]]
    ret = update_two_dim_list([[1],[],[1,2],[1,2,3],[]])
    assert ret == [[1], [1,2],[1,2,3] ]
    ret = update_two_dim_list([[],[]])
    assert ret == []

def test_transpose_two_dim_list():
    ret = transpose_two_dim_list([[1,2], [3,4]])
    assert ret == [[1, 3], [2, 4]]
    ret = transpose_two_dim_list([[1,2,3], [4,5,6]])
    assert ret == [[1, 4], [2, 5], [3, 6]]
    ret = transpose_two_dim_list([[], [3,4]])
    assert ret == None
    ret = transpose_two_dim_list([[1,2], [4,5,6]])
    assert ret == None
    ret = transpose_two_dim_list([[1]])
    assert ret == [[1]]

def test_get_shape_two_dim_list():
    ret = get_shape_two_dim_list([[1,2], [3,4]])
    assert ret == [2, 2]
    ret = get_shape_two_dim_list([[1,2,3], [3,4,6]])
    assert ret == [2, 3]
    ret = get_shape_two_dim_list([[1,2], [3,4,6]])
    assert ret == None

def test_element_wise_add_two_dim_list():
    ret = element_wise_add_two_dim_list([[1,2], [3,4]], [[1,2], [3,4]])
    assert ret == [[2, 4], [6, 8]]
    ret = element_wise_add_two_dim_list([[1], [3,4]], [[1,2], [3,4]])
    assert ret == None
    ret = element_wise_add_two_dim_list([[1, 2], [3,4]], [[], [3,4]])
    assert ret == None
    ret = element_wise_add_two_dim_list([[1, 2, 3], [3, 4, 5]], [[1,2], [3,4]])
    assert ret == None

def test_multiply_two_dim_list():
    ret = multiply_two_dim_list([[1,2], [3,4]], [[5,6], [7,8]])
    assert ret == [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]]
    ret = multiply_two_dim_list([[1], [3,4]], [[5,6], [7,8]])
    assert ret == None
    ret = multiply_two_dim_list([[1, 2], [3,4]], [[5], [7,8]])
    assert ret == None
    ret = multiply_two_dim_list([[1,1,1], [0,0,0]], [[1,2], [3,4], [5,6]])
    assert ret == [[9, 12], [0, 0]]