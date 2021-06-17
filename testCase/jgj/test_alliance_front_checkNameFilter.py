# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 14:19
    @author: by martin
    @description: None
    
"""
import requests
import demjson

from common.loginUtil import Login
from common.getJsonText import GetJsonText
from common.jarUtil import JarUtil
from params.jgjParams import jgj_params

loginKey = Login().jgj_login()

# 敏感词校验,FULL_NAME
def test_alliance_front_checkNameFilter_FULL():
    api_url = "/alliance-front/customer/checkNameFilter"
    uri = jgj_params.urlpre_web + api_url
    str_to_hmac = JarUtil().seqencing([{"loginKey": loginKey, "wordType": "FULL_NAME"}])
    sign = JarUtil().to_hmac(str_to_hmac)
    data = {"loginKey": loginKey, "wordType": "FULL_NAME", "sign": sign}
    rce = requests.post(url=uri, data=data)
    remsg = GetJsonText().get_json_text(demjson.encode(GetJsonText().get_json_text(rce.text, 'data')), "content")
    assert remsg == '开店宝,点佰趣,即富,信托,POS,费率,财富,股票,彩票,证券,银行,债券,基金,期货,外汇,贵金属,融资租赁,有限合伙,资产管理,金融信息,贷款,理财,投资,pos'


# 敏感词校验,SHORT_NAME
def test_alliance_front_checkNameFilter_SHORT():
    api_url = "/alliance-front/customer/checkNameFilter"
    uri = jgj_params.urlpre_web + api_url
    loginKey = Login().jgj_login()
    str_to_hmac = JarUtil().seqencing([{"loginKey": loginKey, "wordType": "SHORT_NAME"}])
    sign = JarUtil().to_hmac(str_to_hmac)
    data = {"loginKey": loginKey, "wordType": "SHORT_NAME", "sign": sign}
    rce = requests.post(url=uri, data=data)
    remsg = GetJsonText().get_json_text(demjson.encode(GetJsonText().get_json_text(rce.text, 'data')), "content")
    assert remsg == '开店宝,点佰趣,即富,信托,POS,费率,财富,股票,彩票,证券,银行,债券,基金,期货,外汇,贵金属,融资租赁,有限合伙,资产管理,金融信息,贷款,理财,投资,pos'


# 敏感词校验,MCC
def test_alliance_front_checkNameFilter_MCC():
    api_url = "/alliance-front/customer/checkNameFilter"
    uri = jgj_params.urlpre_web + api_url
    str_to_hmac = JarUtil().seqencing([{"loginKey": loginKey, "wordType": "MCC"}])
    sign = JarUtil().to_hmac(str_to_hmac)
    data = {"loginKey": loginKey, "wordType": "MCC", "sign": sign}
    rce = requests.post(url=uri, data=data)
    remsg = GetJsonText().get_json_text(demjson.encode(GetJsonText().get_json_text(rce.text, 'data')), "content")
    assert remsg == '6010,6011,6012,6051,6211,5933'
