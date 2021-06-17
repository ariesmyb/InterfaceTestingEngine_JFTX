# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 14:02
    @author: by martin
    @description: None
    
"""
import requests

from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


# 查询动态菜单
def test_app_getMenuList():
    api_url = "/agentmobile/app/getMenuList"
    uri = jgj_params.urlpre + api_url
    data = {'appType': "DTB"}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '查询成功'
