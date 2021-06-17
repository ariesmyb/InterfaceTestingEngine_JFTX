# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 10:22
    @author：by aries
    @description：

"""

from common.getBankCard import GetBankCardSolution
from common.checkOut import CheckOutSolution


# 测试点：随机生成指定cardBin、cardLen的银行卡号，并验证
def test_get_bank_card():
    tcb, tcl = "621256", 19
    test_bank_account = GetBankCardSolution().get_bank_card(card_bin=tcb, card_len=tcl)
    assert CheckOutSolution().check_bank_account(ns=test_bank_account) is True


# 测试点：随机生成指定卡类型（借记卡）的银行卡号，并验证
def test_get_bank_card_4_debit():
    tct = 'debit'
    test_bank_account = GetBankCardSolution().get_bank_card(card_type=tct)
    assert CheckOutSolution().check_bank_account(ns=test_bank_account) is True


# 测试点：随机生成指定卡类型（贷记卡）的银行卡号，并验证
def test_get_bank_card_4_credit():
    tct = 'credit'
    test_bank_account = GetBankCardSolution().get_bank_card(card_type=tct)
    assert CheckOutSolution().check_bank_account(ns=test_bank_account) is True


# 测试点：卡类型赋值取值范围错误
def test_get_bank_card_type_false():
    tct = 'creditt'
    assert GetBankCardSolution().get_bank_card(card_type=tct) is False


# 测试点：cardBin赋值类型错误
def test_get_bank_card_bin_type_false():
    tcb, tcl = 621256, 19
    assert GetBankCardSolution().get_bank_card(card_bin=tcb, card_len=tcl) is False


# 测试点：cardBin赋值取值范围错误
def test_get_bank_card_bin_false():
    tcb, tcl = '6212', 19
    assert GetBankCardSolution().get_bank_card(card_bin=tcb, card_len=tcl) is False


# 测试点：cardLen赋值类型错误
def test_get_bank_card_len_type_false():
    tcb, tcl = '621256', '19'
    assert GetBankCardSolution().get_bank_card(card_bin=tcb, card_len=tcl) is False


# 测试点：cardLen赋值取值范围错误
def test_get_bank_card_len_false():
    tcb, tcl = '621256', 8
    assert GetBankCardSolution().get_bank_card(card_bin=tcb, card_len=tcl) is False
