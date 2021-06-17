# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 14:11
    @author: by martin
    @description: None
    
"""
import requests

from common.loginUtil import Login
from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


# 设置品牌
def test_setBrand():
    api_url = "/agentmobile/dtb/setBrand"
    uri = jgj_params.urlpre + api_url
    data = {'loginKey': Login().jgj_login(), 'phoneMAC': jgj_params.phoneMAC, 'brandCode': jgj_params.brandCode}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '设置成功！'

