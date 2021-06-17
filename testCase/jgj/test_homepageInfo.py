# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 14:06
    @author: by martin
    @description: None
    
"""
import requests

from common.getJsonText import GetJsonText
from common.loginUtil import Login
from params.jgjParams import jgj_params


# 查询主页基本信息
def test_homepageInfo():
    api_url = "/agentmobile/dtb/homepageInfo"
    uri = jgj_params.urlpre + api_url
    data = {'loginKey': Login().jgj_login(), 'phoneMAC': jgj_params.phoneMAC, 'brandCode': jgj_params.brandCode}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['code'])
    assert msg[0] == '00'
