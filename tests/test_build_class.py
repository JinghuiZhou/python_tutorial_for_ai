import os.path
import sys
import json
sys.path.append(".")
from basic.build_class import *

obj = None

def test_init():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    assert obj.param == {
      "hello": "world",
      "foo": "bar"
    }
    obj = AisDeployInterface("{\"hello\":\"world\"}")
    assert obj.param == {
        "hello": "world"
    }

def test_del():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    obj.__del__()
    assert obj.param == None

def test_get_param():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    assert obj.get_param() == {
      "hello": "world",
      "foo": "bar"
    }
    obj = AisDeployInterface("{\"hello\":\"world\"}")
    assert obj.get_param() == {
        "hello": "world"
    }

def test_get_param_str():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    assert obj.get_param_str()
    obj = AisDeployInterface("{\"hello\":\"world\"}")
    assert obj.get_param_str()

def test_update_param():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    obj.update_param({"hello":"world"})
    assert obj.param == {
      "hello": "world",
      "foo": "bar"
    }
    obj = AisDeployInterface("{\"hello\":\"world\"}")
    obj.update_param({"1":"2"})
    assert obj.param == {
        "hello": "world",
        "1": "2"
    }

def test_delete_key():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    obj.delete_key("hello")
    assert obj.param == {
      "foo": "bar"
    }
    obj = AisDeployInterface("{\"hello\":\"world\"}")
    obj.delete_key("hello")
    assert obj.param == {}

def test_cal_str_distance():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    assert obj.cal_str_distance("hello", "hello") == 0.0
    assert obj.cal_str_distance("hello", "world") > 0.5
    assert obj.cal_str_distance("a", "a") == 0.0
    assert obj.cal_str_distance("a", "b") > 0.5

def test_process():
    global obj
    obj = AisDeployInterface("tests/assets/class_init1.json")
    input_dict = {"input": "hello"}
    assert obj.process(input_dict) == "world"
    input_dict = {"input": "hell"}
    assert obj.process(input_dict) == "world"
    input_dict = {"input": "a"}
    assert obj.process(input_dict) == "a"


