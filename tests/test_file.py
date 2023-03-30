import os.path
import sys
import json
sys.path.append(".")
from basic.file import *

path_tmp = __file__.replace(__file__.split("/")[-1], "")

def test_read_txt_file():
    ret = read_txt_file("tests/assets/1.txt")
    assert ret == ["1", "2", "3"]
    ret = read_txt_file("tests/assets/_1.txt")
    assert ret == list()

def test_write_txt_file():
    l = ["1", "3", "2"]
    write_txt_file("tests/assets/_2.txt", l)
    ret = read_txt_file("tests/assets/_2.txt")
    assert ret == l


def test_read_json_file():

    ret = read_json_file("tests/assets/1.json")
    assert json.loads(ret) == [{"name": "123","major": "ai"}]
    ret = read_json_file("tests/assets/_1.json")
    assert ret is None

def test_write_json_file():
    ds = [
        dict(name="1", value=2),
        dict(name="2", value=3)
    ]
    write_json_file("tests/assets/_2.json", ds)
    ret = read_json_file("tests/assets/_2.json")
    assert json.loads(ret)==[dict(value=2), dict(value=3)]

# read_xml_file(path: str)的单元测试
def test_read_xml_file():
    ret = read_xml_file("tests/assets/2007_001225.xml")
    assert type(ret) == str
    assert json.loads(ret) == json.loads("{\"annotation\":{\"folder\":\"VOC2012\",\"filename\":\"2007_001225.jpg\",\"source\":{\"database\":\"The VOC2007 Database\",\"annotation\":\"PASCAL VOC2007\",\"image\":\"flickr\"},\"size\":{\"width\":\"387\",\"height\":\"500\",\"depth\":\"3\"},\"segmented\":\"1\",\"object\":{\"name\":\"dog\",\"pose\":\"Frontal\",\"truncated\":\"1\",\"difficult\":\"0\",\"bndbox\":{\"xmin\":\"100\",\"ymin\":\"212\",\"xmax\":\"303\",\"ymax\":\"414\"}}}}")

    ret = read_xml_file("tests/assets/2007_001185.xml")
    assert type(ret) == str
    assert json.loads(ret) == json.loads(
        "{\"annotation\":{\"folder\":\"VOC2012\",\"filename\":\"2007_001185.jpg\",\"source\":{\"database\":\"The VOC2007 Database\",\"annotation\":\"PASCAL VOC2007\",\"image\":\"flickr\"},\"size\":{\"width\":\"500\",\"height\":\"375\",\"depth\":\"3\"},\"segmented\":\"1\",\"object\":[{\"name\":\"cat\",\"pose\":\"Frontal\",\"truncated\":\"1\",\"difficult\":\"0\",\"bndbox\":{\"xmin\":\"197\",\"ymin\":\"199\",\"xmax\":\"289\",\"ymax\":\"323\"}},{\"name\":\"person\",\"pose\":\"Frontal\",\"truncated\":\"1\",\"difficult\":\"0\",\"bndbox\":{\"xmin\":\"78\",\"ymin\":\"78\",\"xmax\":\"289\",\"ymax\":\"375\"}},{\"name\":\"diningtable\",\"pose\":\"Unspecified\",\"truncated\":\"1\",\"difficult\":\"1\",\"bndbox\":{\"xmin\":\"204\",\"ymin\":\"223\",\"xmax\":\"500\",\"ymax\":\"375\"}},{\"name\":\"bottle\",\"pose\":\"Unspecified\",\"truncated\":\"1\",\"difficult\":\"0\",\"bndbox\":{\"xmin\":\"452\",\"ymin\":\"131\",\"xmax\":\"500\",\"ymax\":\"253\"}}]}}")

# write_xml_file(path: str, ds:List[Dict])的单元测试
def test_write_xml_file():
    ds = [
        dict(name="1", value=2),
        dict(name="2", value=3)
    ]
    write_xml_file("tests/assets/_2.xml", ds)
    ret = read_xml_file("tests/assets/_2.xml")
    assert json.loads(ret) == json.loads("{\"root\":{\"item\":[{\"name\":\"1\",\"value\":\"2\"},{\"name\":\"2\",\"value\":\"3\"}]}}")

    ds = [
        dict(name="3", value=2),
        dict(name="4", value=3)
    ]
    write_xml_file("tests/assets/_2.xml", ds)
    ret = read_xml_file("tests/assets/_2.xml")
    assert json.loads(ret) == json.loads(
        "{\"root\":{\"item\":[{\"name\":\"3\",\"value\":\"2\"},{\"name\":\"4\",\"value\":\"3\"}]}}")

# def read_csv_file(path: str)的单元测试
def test_read_csv_file():
    ret = read_csv_file("tests/assets/data_x_x2_x3.csv")
    assert ret == [['0', '0', '0'], ['1', '1', '1'], ['2', '4', '8'], ['3', '9', '27'], ['4', '16', '64'], ['5', '25', '125'], ['6', '36', '216'], ['7', '49', '343'], ['8', '64', '512'], ['9', '81', '729'], ['10', '100', '1000']]
    ret = read_csv_file("tests/assets/data_x_x2_x4.csv")
    assert ret == [['0', '0', '0'], ['1', '1', '2'], ['2', '4', '4'], ['3', '9', '2'], ['4', '16', '6'], ['5', '25', '125'], ['6', '36', '216'], ['7', '49', '343'], ['8', '64', '512'], ['9', '81', '729'], ['10', '100', '1000']]
