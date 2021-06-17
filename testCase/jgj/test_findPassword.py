# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-16 14:19
    @author: by aries
    @description: None
    
"""
import pytest
import requests

from common.getJsonText import GetJsonText
from common.getRandomNumber import GetRandomNumberSolution
from common.logParameter import LogParameterSolution
from common.redisSentinelHelper import get_redis
from params.jgjParams import jgj_params


def sendCheckCodeFindPwd():
    api_url = "/agentmobile/dtb/sendCheckCodeFindPwd"
    uri = jgj_params.urlpre + api_url
    data = {'mobile': jgj_params.mobile_findpwd}
    requests.post(url=uri, data=data)
    codeLocal_FindPwd = get_redis('AGENT_CHECK_CODE' + jgj_params.mobile_findpwd, 3)
    if codeLocal_FindPwd is None:
        LogParameterSolution().error("验证码为：空")
    else:
        LogParameterSolution().info("忘记密码验证码为：" + codeLocal_FindPwd)
    return codeLocal_FindPwd

api_url = "/agentmobile/dtb/findPassword"


# 忘记密码，修改密码，成功
@pytest.mark.run(order=4)
def test_findPassword():
    uri = jgj_params.urlpre + api_url
    codeLocal_FindPwd = get_redis('AGENT_CHECK_CODE' + jgj_params.mobile_findpwd, 3)
    data = {'mobile': jgj_params.mobile_findpwd, 'verificationCode': codeLocal_FindPwd, 'password': jgj_params.password_find}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '密码修改成功！'


# 忘记密码，修改密码，手机号未注册
@pytest.mark.run(order=2)
def test_findPassword_Mobile_Error():
    uri = jgj_params.urlpre + api_url
    data = {'mobile': GetRandomNumberSolution().get_phone_number(), 'verificationCode': sendCheckCodeFindPwd(), 'password': jgj_params.password_old}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '该手机号没有注册！'


# 忘记密码，修改密码，验证码不正确
@pytest.mark.run(order=3)
def test_findPassword_VerificationCode_Error():
    uri = jgj_params.urlpre + api_url
    data = {'mobile': jgj_params.mobile_findpwd, 'verificationCode': GetRandomNumberSolution().get_random_number_4_dt(time_format="%H%M%S"), 'password': jgj_params.password_old}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '验证码不正确！'


# 忘记密码，修改密码，验证码已使用
@pytest.mark.run(order=5)
def test_findPassword_VerificationCode():
    uri = jgj_params.urlpre + api_url
    data = {'mobile': jgj_params.mobile_findpwd, 'verificationCode': get_redis('AGENT_CHECK_CODE' + jgj_params.mobile_findpwd, 3), 'password': jgj_params.password_old}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    print(rce.text)
    assert msg[0] == '验证码已经过期，请重新获取验证码！'


# 忘记密码，修改密码，验证码为空
@pytest.mark.run(order=1)
def test_findPassword_VerificationCode_None():
    uri = jgj_params.urlpre + api_url
    data = {'mobile': jgj_params.mobile_findpwd, 'verificationCode': None, 'password': jgj_params.password_old}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['showMsg'])
    assert msg[0] == '验证码不能为空'
