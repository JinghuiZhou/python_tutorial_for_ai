import os.path
import sys
import json
sys.path.append(".")
from basic.file import *

path_tmp = __file__.replace(__file__.split("/")[-1], "")

def test_read_txt_file():
    ret = read_txt_file(os.path.join(path_tmp,"assets/1.txt"))
    assert ret == ["1", "2", "3"]
    ret = read_txt_file("tests/assets/_1.txt")
    assert ret == list()

def test_write_txt_file():
    l = ["1", "3", "2"]
    write_txt_file(os.path.join(path_tmp,"assets/_2.txt"), l)
    ret = read_txt_file(os.path.join(path_tmp,"assets/_2.txt"))
    assert ret == l


def test_read_json_file():
    path_tmp = __file__.replace(__file__.split("/")[-1], "")
    ret = read_json_file(os.path.join(path_tmp,"assets/1.json"))
    assert json.loads(ret) == [{"name": "123","major": "ai"}]
    ret = read_txt_file("tests/assets/_1.json")
    assert ret is None

def test_write_json_file():
    path_tmp = __file__.replace(__file__.split("/")[-1], "")
    ds = [
        dict(name="1", value=2),
        dict(name="2", value=3)
    ]
    write_json_file(os.path.join(path_tmp,"assets/_2.json"), ds)
    ret = read_json_file(os.path.join(path_tmp,"assets/_2.json"))
    assert json.loads(ret)==[dict(value=2), dict(value=3)]