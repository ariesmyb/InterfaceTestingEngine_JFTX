# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 14:29
    @author: by martin
    @description: None
    
"""
import requests

from common.loginUtil import Login
from common.getJsonText import GetJsonText
from common.jarUtil import JarUtil
from params.jgjParams import jgj_params


# 获取支行信息
def test_customer_findAllBranchInfo():
    api_url = "/alliance-front/customer/findAllBranchInfo"
    uri = jgj_params.urlpre_web + api_url
    loginKey = Login().jgj_login()
    str_to_hmac = JarUtil().seqencing([{"loginKey": loginKey, "bankCode": "ICBC", "bankName": "宣武门", "lefuAreaCode": "1101"}])
    sign = JarUtil().to_hmac(str_to_hmac)
    data = {"loginKey": loginKey, "bankCode": "ICBC", "bankName": "宣武门", "lefuAreaCode": "1101", "sign": sign}
    rce = requests.post(url=uri, data=data)
    msg = GetJsonText().get_json_text_by_list(rce.text, ['msg'])
    assert msg[0] == '查询成功'
