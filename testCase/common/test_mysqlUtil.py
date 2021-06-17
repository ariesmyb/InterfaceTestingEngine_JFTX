# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-08 14:34
    @author: by aries
    @description: None
    
"""
from common.mysqlUtil import MysqlUtil
from params.dbConfig import *


def test_mysql_insert():
    mysql = MysqlUtil('192.168.6.46')
    mysql.execute_sql("INSERT INTO settle.settle_card (id, optimistic, owner_id, owner_role, card_type, bank_account_name, bank_account_no, bank_code, bank_name, allied_bank_code, sabk_code, own_bank_code, province, city, eff_date, exp_date, status, priority, last_update_date, create_date, need_bill, bill_header_name, account_no, sign, memo, card_bin, card_category, org_id, card_no_ciphertext) VALUES ('SC33333333', 0, '8625832215', 'AGENT', 'OPEN', '北京即富天下科技有限公司06', '6222021950544454018', 'ICBC', '中国工商银行北京市分行清算中心', '102100009980', '102100099996', null, '北京', '北京', '2020-09-03', '2099-12-31', 'ENABLE', 0, '2020-09-04 16:16:30', '2020-09-04 16:16:30', 0, null, null, 'c06b50c1edfcb2434342f4453a485cdd', null, null, 'DEBIT', null, '545453121213231')")
    result = mysql.select_data("select bank_account_no from settle.settle_card where id='SC33333333'")
    mysql.close_db()
    assert result[0][0] == '6222021950544454018'


def test_mysql_update():
    mysql = MysqlUtil('192.168.6.46')
    mysql.execute_sql("update settle.settle_card set bank_code='ABC' where id='SC33333333'")
    result = mysql.select_data("select bank_code from settle.settle_card where id='SC33333333'")
    mysql.close_db()
    assert result[0][0] == 'ABC'


def test_mysql_delete():
    mysql = MysqlUtil('192.168.6.46')
    mysql.execute_sql("delete from  settle.settle_card  where id='SC33333333'")
    result = mysql.select_data("select * from settle.settle_card where id='SC33333333'")
    mysql.close_db()
    assert result == ()
