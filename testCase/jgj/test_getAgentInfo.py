# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 13:57
    @author: by martin
    @description: None
    
"""
import requests

from common.getJsonText import GetJsonText
from common.loginUtil import Login
from params.jgjParams import jgj_params


# 查询服务商信息
def test_getAgentInfo():
    api_url = "/agentmobile/dtb/getAgentInfo"
    uri = jgj_params.urlpre + api_url
    data = {'loginKey': Login().jgj_login(), 'phoneMAC': jgj_params.phoneMAC}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['code'])
    assert msg[0] == '00'

