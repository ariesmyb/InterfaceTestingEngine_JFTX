# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-16 14:09
    @author: by aries
    @description: None
    
"""
import requests

from common.loginUtil import Login
from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


# 登出
def test_logout():
    api_url = "/agentmobile/dtb/logout"
    uri = jgj_params.urlpre + api_url
    data = {'loginKey': Login().jgj_login()}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '退出成功！'
