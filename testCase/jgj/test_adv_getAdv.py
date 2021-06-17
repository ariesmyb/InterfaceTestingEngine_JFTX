# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 11:18
    @author: by martin
    @description: None
    
"""
import requests

from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


# 查询广告banner页
def test_adv_getAdv():
    api_url = "/agentmobile/adv/getAdv"
    uri = jgj_params.urlpre + api_url
    data = {'appType': "DTB"}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '查询成功'
