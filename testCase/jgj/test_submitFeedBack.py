# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 14:13
    @author: by martin
    @description: None
    
"""
import requests

from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


# 用户意见反馈
def test_submitFeedBack():
    api_url = "/agentmobile/dtb/submitFeedBack"
    uri = jgj_params.urlpre + api_url
    data = {"phone": "18444231527", "isAnonymous": "1", "content&": "用户意见反馈内容HTTP://www.baidu.com"}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '提交成功！'
