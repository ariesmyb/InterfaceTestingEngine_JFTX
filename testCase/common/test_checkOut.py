# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 10:27
    @author：by aries
    @description：

"""

import os, pytest
from common.toPath import ToPathSolution
from common.checkOut import CheckOutSolution

test_path = str(ToPathSolution().Users.aries.Documents.GitHub.TestDemo.logs)


# 测试点：两文件MD5值对比一致
@pytest.mark.run(order=5)
def test_check_file_md5():
    f1 = os.path.join(test_path, "2020-06-04.log")
    f2 = os.path.join(test_path, "2020-06-04.log")
    assert CheckOutSolution().check_file_md5(fs1=f1, fs2=f2) is True


# 测试点：两文件MD5值对比不一致
@pytest.mark.run(order=6)
def test_check_file_md5_false():
    f1 = os.path.join(test_path, "2020-06-02.log")
    f3 = os.path.join(test_path, "2020-06-04.log")
    assert CheckOutSolution().check_file_md5(fs1=f1, fs2=f3) is False


# 测试点：tval包含ts
@pytest.mark.run(order=1)
def test_assert_embody():
    ts = 's'
    val = 'skkk'
    assert CheckOutSolution().embody(s=ts, val=val) is True


# 测试点：tval不包含ts
@pytest.mark.run(order=2)
def test_assert_embody_false():
    ts = 's'
    val = 'kkk'
    assert CheckOutSolution().embody(s=ts, val=val) is False


# 测试点：非银行卡号验证结果
@pytest.mark.last
def test_check_bank_account_false():
    bank_account = "6244540070961874"
    assert CheckOutSolution().check_bank_account(ns=bank_account) is False


# 测试点：银行卡号验证结果
@pytest.mark.run(order=4)
def test_check_bank_account():
    bank_account = "6231551591256417"
    assert CheckOutSolution().check_bank_account(ns=bank_account) is True


# 测试点：银行卡号验证，赋值类型错误
@pytest.mark.run(order=3)
def test_check_bank_account_type_false():
    bank_account = 6231551591256417
    assert CheckOutSolution().check_bank_account(ns=bank_account) is False
