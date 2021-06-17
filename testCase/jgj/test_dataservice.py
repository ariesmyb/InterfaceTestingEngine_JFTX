# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 13:48
    @author: by martin
    @description: None
    
"""
import requests

from params.jgjParams import jgj_params


# 获取省份信息
def test_dataservice_getAllProvinceByJson():
    api_url = "getAllProvinceByJson?callback"
    uri = jgj_params.urlpre_dataserive + api_url
    rce = requests.get(url=uri)
    assert "河北" in rce.text


# 获取城市信息
def test_dataservice_getCityByJson():
    api_url = "getCityByJson/13?callback"
    uri = jgj_params.urlpre_dataserive + api_url
    rce = requests.get(url=uri)
    assert "邢台市" in rce.text


# 获取区县信息
def test_dataservice_getDistrictByJson():
    api_url = "getDistrictByJson/3101?callback"
    uri = jgj_params.urlpre_dataserive + api_url
    rce = requests.get(url=uri)
    print(rce.text)
    assert "普陀区" in rce.text
