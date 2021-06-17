# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 10:04
    @author：by aries
    @description：

"""

from common.getIDCard import GetIDCardSolution


# 测试点：随机生成身份证号
def test_get_id_card():
    assert len(GetIDCardSolution().get_id_card()) == 18


# 测试点：指定地域随机生成身份证号
def test_get_id_card_regional_number():
    trni = 130105
    assert GetIDCardSolution().get_id_card(rni=trni)[0:6] == str(trni)


# 测试点：指定地域赋值长度错
def test_get_id_card_regional_number_len_false():
    trni = 1301059
    assert GetIDCardSolution().get_id_card(rni=trni) is False


# 测试点：指定地域赋值类型错
def test_get_id_card_regional_number_type_false():
    trni = "130105"
    assert GetIDCardSolution().get_id_card(rni=trni) is False


# 测试点：指定年份随机生成身份证号
def test_get_id_card_year():
    tyi = 1985
    assert GetIDCardSolution().get_id_card(yi=tyi)[6:10] == str(tyi)


# 测试点：指定月份随机生成身份证号
def test_get_id_card_month():
    tmi = 4
    if tmi < 10:
        tms = '0' + str(tmi)
    else:
        tms = str(tmi)
    assert GetIDCardSolution().get_id_card(mi=tmi)[10:12] == tms


# 测试点：指定月份赋值超出取值范围
def test_get_id_card_month_false():
    tmi = 40
    assert GetIDCardSolution().get_id_card(mi=tmi) is False


# 测试点：指定月份赋值类型范围
def test_get_id_card_month_type_error():
    tmi = '2'
    assert GetIDCardSolution().get_id_card(mi=tmi) is False


# 测试点：指定日期随机生成身份证号
def test_get_id_card_day():
    tdi = 21
    if tdi < 10:
        tds = '0' + str(tdi)
    else:
        tds = str(tdi)
    assert GetIDCardSolution().get_id_card(di=tdi)[12:14] == tds


# 测试点：指定月份赋值超出取值范围
def test_get_id_card_day_error():
    tdi = 40
    assert GetIDCardSolution().get_id_card(mi=tdi) is False


# 测试点：指定月份赋值类型范围
def test_get_id_card_day_type_error():
    tdi = '2'
    assert GetIDCardSolution().get_id_card(mi=tdi) is False


# 测试点：指定出生日期随机生成身份证号
def test_get_id_card_ymd():
    tyi, tmi, tdi = 1984, 1, 28
    if tmi < 10:
        tms = '0' + str(tmi)
    else:
        tms = str(tmi)
    if tdi < 10:
        tds = '0' + str(tdi)
    else:
        tds = str(tdi)
    assert GetIDCardSolution().get_id_card(yi=tyi, mi=tmi, di=tdi)[6:14] == str(tyi) + tms + tds


# 测试点：指定性别（男）随机生成身份证号
def test_get_id_card_sex_male():
    tron, sex = 1, 'male'
    if int(GetIDCardSolution().get_id_card(rsni=tron)[-2]) % 2 == 0:
        sex = 'female'
    else:
        sex = 'male'
    assert sex == sex


# 测试点：指定性别（女）随机生成身份证号
def test_get_id_card_sex_female():
    transit, sex = 0, 'female'
    if int(GetIDCardSolution().get_id_card(rsni=transit)[-2]) % 2 == 0:
        sex = 'female'
    else:
        sex = 'male'
    assert sex == sex


# 测试点：指定性别赋值类型错误
def test_get_id_card_sex_false():
    trains = 11
    assert GetIDCardSolution().get_id_card(rsni=trains) is False


# 测试点：指定性别赋值超出取值范围
def test_get_id_card_sex_type_false():
    train = '1'
    assert GetIDCardSolution().get_id_card(rsni=train) is False
