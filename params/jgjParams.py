# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-15 14:25
    @author: by aries
    @description: None
    
"""
import random

from common.oracleUtil import OracleUtil


class jgj_params:
    oral = OracleUtil('posp_agent')
    username = oral.select_data("select USERNAME from POSP_AGENT.OPERATOR where STATUS='TRUE' and PASSWORD='18a49c364ba10330d894b11652e65bc2'")
    oral.close_db()


    # 原生接口URL前缀
    urlpre = "http://192.168.5.38:8085"
    urlpre_dataserive = "https://v.91dbq.com/dataservice/"
    urlpre_web = "http://192.168.5.38:8082"

    # mobile_findpwd = '17657020502'
    mobile_findpwd = username[random.randint(0, len(username)-1)][0]
    mobile_agent_up = "18899990000"

    password_find = "1111aaaa@@"
    password_old = "12345Qwert"

    brandCode = "DIANPAY"

    phoneMAC = "874C9D3C-0563-4E24-A1E4-B57BD143EBF8"
