# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-16 11:12
    @author: by aries
    @description: None
    
"""
import requests

from common.loginUtil import Login
from common.getRandomNumber import GetRandomNumberSolution
from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


# 登陆成功
def test_login():
    uri = jgj_params.urlpre + Login().jgj_api_url
    data = {'mobile': jgj_params.mobile_agent_up, 'password': jgj_params.password_old, 'phoneMAC': jgj_params.phoneMAC}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '用户验证成功！'


# 登陆失败，手机号错
def test_login_mobile_error():
    uri = jgj_params.urlpre + Login().jgj_api_url
    data = {'mobile': GetRandomNumberSolution().get_phone_number(), 'password': jgj_params.password_old, 'phoneMAC': jgj_params.phoneMAC}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '用户名或密码错误'


# 登陆失败，手机号空
def test_login_mobile_none():
    uri = jgj_params.urlpre + Login().jgj_api_url
    data = {'mobile': None, 'password': jgj_params.password_old, 'phoneMAC': jgj_params.phoneMAC}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '手机号或者设备号为空'


# 登陆失败，密码错
def test_login_password_error():
    uri = jgj_params.urlpre + Login().jgj_api_url
    data = {'mobile': jgj_params.mobile_agent_up, 'password': GetRandomNumberSolution().get_random_number_4_dt(time_format="%H%M%S"), 'phoneMAC': jgj_params.phoneMAC}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '用户名或密码错误'


# 登陆失败，密码空
def test_login_password_none():
    uri = jgj_params.urlpre + Login().jgj_api_url
    data = {'mobile': jgj_params.mobile_agent_up, 'password': None, 'phoneMAC': jgj_params.phoneMAC}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '密码格式错误'
