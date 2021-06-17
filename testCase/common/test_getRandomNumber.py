# -*- coding: UTF-8 -*-

"""
    @create：5/21/20 14:48
    @author：by aries
    @description：

"""

from common.getRandomNumber import GetRandomNumberSolution


# 测试点：随机数，全长为20
def test_get_random_number_4_dt():
    assert len(GetRandomNumberSolution().get_random_number_4_dt()) == 20


# 测试点：随机数，指定到秒，全长为14
def test_get_random_number_4_dt_format_ymdhms():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%Y%m%d%H%M%S")) == 14


# 测试点：随机数，指定为毫秒，全长为6
def test_get_random_number_4_dt_format_f():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%f")) == 6


# 测试点：随机数，指定到分，全长为12
def test_get_random_number_4_dt_format_ymdhm():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%Y%m%d%H%M")) == 12


# 测试点：随机数，指定到日，全长为8
def test_get_random_number_4_dt_format_ymd():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%Y%m%d")) == 8


# 测试点：随机数，指定为月日，全长为4
def test_get_random_number_4_dt_format_md():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%m%d")) == 4


# 测试点：随机数，指定为时分，全长为4
def test_get_random_number_4_dt_format_hm():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%H%M")) == 4


# 测试点：随机数，指定为时分秒，全长为6
def test_get_random_number_4_dt_format_hms():
    assert len(GetRandomNumberSolution().get_random_number_4_dt(time_format="%H%M%S")) == 6


# 测试点：随机生成年
def test_get_random_year():
    assert len(str(GetRandomNumberSolution().get_random_year())) == 4


# 测试点：随机生成，指定生成年
def test_get_random_year_yi():
    tyi = 1983
    assert (GetRandomNumberSolution().get_random_year(yi=tyi)) == tyi


# 测试点：随机生成年，赋值类型错误
def test_get_random_year_yi_type_false():
    tyi = '1983'
    assert GetRandomNumberSolution().get_random_year(yi=tyi) is False


# 测试点：随机生成月份
def test_get_random_month_len():
    assert len(str(GetRandomNumberSolution().get_random_month())) == 2


# 测试点：随机生成指定月份
def test_get_random_month_mi():
    tmi = 4
    if tmi < 10:
        tms = '0' + str(tmi)
    else:
        tms = tmi
    assert GetRandomNumberSolution().get_random_month(mi=tmi) == tms


# 测试点：指定月份赋值超出取值范围
def test_get_random_month_false():
    tmi = 13
    assert GetRandomNumberSolution().get_random_month(mi=tmi) is False


# 测试点：指定月份赋值类型范围
def test_get_random_month_type_false():
    tmi = '2'
    assert GetRandomNumberSolution().get_random_month(mi=tmi) is False


# 测试点：随机生成日
def test_get_random_day():
    assert len(str(GetRandomNumberSolution().get_random_day())) == 2


# 测试点：随机生成指定日
def test_get_random_day_d():
    tdi = 11
    if tdi < 10:
        tds = '0' + str(tdi)
    else:
        tds = tdi
    assert GetRandomNumberSolution().get_random_day(di=tdi) == tds


# 测试点：随机生成日，按指定年、月
def test_get_random_day_ym():
    assert len(str(GetRandomNumberSolution().get_random_day(yi=2000, mi=2))) == 2


# 测试点：指定月份赋值超出取值范围
def test_get_random_day_false():
    tdi = 40
    assert GetRandomNumberSolution().get_random_day(di=tdi) is False


# 测试点：指定月份赋值类型范围
def test_get_random_day_type_false():
    tdi = '2'
    assert GetRandomNumberSolution().get_random_day(di=tdi) is False


# 测试点：指定月、日错误
def test_get_random_day_md_false():
    tyi, tdi = 4, 31
    assert GetRandomNumberSolution().get_random_day(mi=tyi, di=tdi) is False


# 测试点：指定年、月、日错误
def test_get_random_day_ymd_false():
    tyi, tmi, tdi = 2001, 2, 29
    assert GetRandomNumberSolution().get_random_day(yi=tyi, mi=tmi, di=tdi) is False


# 测试点：随机生成手机号
def test_get_phone_number():
    assert len(GetRandomNumberSolution().get_phone_number()) == 11


# 测试点：随机生成手机号，指定号段
def test_get_phone_number_segment():
    timpani = 31
    assert len(GetRandomNumberSolution().get_phone_number(pni=timpani)) == 11


# 测试点：随机生成手机号，指定号段赋值类型错误
def test_get_phone_number_segment_type_false():
    timpani = '31'
    assert GetRandomNumberSolution().get_phone_number(pni=timpani) is False


# 测试点：随机生成手机号，指定号段赋值长度错误
def test_get_phone_number_segment_false():
    timpani = 31234574628
    assert GetRandomNumberSolution().get_phone_number(pni=timpani) is False
