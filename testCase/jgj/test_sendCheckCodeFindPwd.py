# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-15 14:23
    @author: by aries
    @description: None
    
"""
import requests

from common.getRandomNumber import GetRandomNumberSolution
from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params

api_url = "/agentmobile/dtb/sendCheckCodeFindPwd"


# 忘记密码发送短信，成功
def test_sendCheckCodeFindPwd():
    uri = jgj_params.urlpre + api_url
    data = {'mobile': jgj_params.mobile_findpwd}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == "00"


# 忘记密码发送短信，手机号未注册
def test_sendCheckCodeFindPwd_Mobile_Error():
    uri = jgj_params.urlpre + api_url
    new_mobile = GetRandomNumberSolution().get_phone_number()
    data = {'mobile': new_mobile}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '该手机号没有注册！'
