# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 13:57
    @author: by aries
    @description: None
    
"""
import demjson
import requests
from common.getJsonText import GetJsonText
from params.jgjParams import jgj_params


class Login:
    def __init__(self):
        self.jgj_api_url = "/agentmobile/dtb/login"

    def jgj_login(self):
        uri = jgj_params.urlpre + self.jgj_api_url
        data = {'mobile': jgj_params.mobile_agent_up, 'password': jgj_params.password_old, 'phoneMAC': jgj_params.phoneMAC}
        rce = requests.post(url=uri, data=data)
        loginKey = GetJsonText().get_json_text(demjson.encode(GetJsonText().get_json_text(rce.text, 'data')), "loginKey")
        return loginKey
