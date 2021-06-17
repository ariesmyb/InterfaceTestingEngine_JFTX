# -*- coding: UTF-8 -*-

"""
    @create：5/19/20 09:45
    @author：by aries
    @description：

"""

from common.encryptionUtil import EncryptionUtilSolution


# 测试点：字符串md5加密值一致
def test_md5Util():
    val = '1111aaaa'
    val2 = 'd41d8cd98f00b204e9800998ecf8427e'
    assert EncryptionUtilSolution().md5_util(s=val) == val2


# 测试点：字符串md5加密值不一致
def test_md5Util_false():
    val = '1111aaaa'
    val2 = 'd41d8cd98f00b204e9800998ecf8427'
    assert EncryptionUtilSolution().md5_util(s=val) != val2


# 测试点：Hmac加密
def test_hmacUtil():
    s = '1111aaaa'
    hmac_type = "sha1"
    val = {
        "md5": "0c9bf819f1b8ed28592dcb24c5554045",
        "sha1": "4019339d5ba5bbfb373692a4f2e0760810885aa8",
        "sha256": "61b2603e5770090a191d7b0fa6cbb9878106b472c6c7dc3f52254f3f6505546c",
        "sha384": "b26d1056117b05a2661b32edd64813fb4778774fea9000cdb22e81800a4db5f01a1fa1fa9b75728e2c0c13e37accbb7c",
        "sha512": "a0d3c1ba6c571950e52f841dc6218eee5c7ce2cad321a1eece201a6970584ed4ce58a5c9800e0d5812d15e8831d169ad13bf38ab4d9ab8a2717efa9ea19876b9"
    }
    assert EncryptionUtilSolution().hmac_util(s=s, type=hmac_type) == val[hmac_type]


# 测试点：base64加密
def test_base64Util():
    s = '1111aaaa'
    val = b'MTExMWFhYWE='
    assert EncryptionUtilSolution().base64_util(body_str=s) == val


# 测试点：base64解密
def test_base64_decode():
    val = b'MTExMWFhYWE='
    s = '1111aaaa'
    assert EncryptionUtilSolution().base64_util_decode(body_str=val) == s
