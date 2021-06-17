# -*- coding: UTF-8 -*-

"""
    @create：5/20/20 14:38
    @author：by aries
    @description：

"""

from common.stringUtil import StringUtilSolution

test_str = "843181056160351363"
test_hex = "413230363730313030323032303230313830303030303630323632323030303032313530333030363930393737383034303038393841343844453330353030383230303232303031"


# 测试点：isChinese为True
def test_is_chinese():
    test_strc = u'\u4e99'
    assert StringUtilSolution().is_chinese(s=test_strc) is True


# 测试点：isChinses赋值超出取值范围
def test_is_chinese_false():
    test_strc = u'\u4b99'
    assert StringUtilSolution().is_chinese(s=test_strc) is False


# 测试点：字符串转16进制
def test_convert_string_2_hex():
    val = '383433313831303536313630333531333633'
    assert StringUtilSolution().convert_string_2_hex(s=test_str) == val


# 测试点：字符串转16进制，赋值类型错误
def test_convert_string_2_hex_tpye_false():
    tsi = int(test_str)
    assert StringUtilSolution().convert_string_2_hex(s=tsi) is False


# 测试点：16进制转字符串
def test_convert_hex_2_string():
    var = 'A2067010020202018000006026220000215030069097780400898A48DE30500820022001'
    assert StringUtilSolution().convert_hex_2_string(hs=test_hex) == var


# 测试点：16进制转字符串，赋值类型错误
def test_convert_hex_2_string_false():
    thi = int(test_hex)
    assert StringUtilSolution().convert_hex_2_string(hs=thi) is False


# 测试点：字符串（含中文）长度
def test_get_string_len():
    ts = "接口测试demo"
    assert StringUtilSolution().get_string_len(s=ts) == 12


# 测试点：字符串长度，赋值类型错误
def test_get_string_len_type_false():
    ts = 677774
    assert StringUtilSolution().get_string_len(s=ts) is False


# 测试点：随机生成8位16进制字符串
def test_random_hex_string():
    assert len(StringUtilSolution().random_hex_string()) == 8


# 测试点：随机生成指定位数的16进制字符串
def test_random_hex_string_4_hi():
    thi = 16
    assert len(StringUtilSolution().random_hex_string(hi=thi)) == 16


# 测试点：随机生成指定位数的16进制字符串，赋值类型错误
def test_random_hex_string_type_false():
    thi = '16'
    assert StringUtilSolution().random_hex_string(hi=thi) is False
