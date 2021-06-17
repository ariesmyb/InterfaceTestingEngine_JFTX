# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-04 14:35
    @author: by aries
    @description: None
    
"""

from common.oracleUtil import OracleUtil


def test_oracle_insert():
    oral = OracleUtil('posp_agent')
    oral.execute_sql("INSERT INTO POSP_AGENT.OPERATOR (ID, OPTIMISTIC, USERNAME, STATUS, PASSWORD, MAX_ERROR_TIMES, LAST_LOGIN_ERR_TIME, MODIFY_PASSWD_CYCLE, PASSWD_MODIFY_TIME, ALLOW_BEGIN_TIME, ALLOW_END_TIME, OPERATOR_TYPE, REALNAME, CREATE_TIME, CREATE_OPERATOR, RELOGIN_FLAG, PASSWD_EXPIRE_TIME, PASSWD_EFFECT_TIME, TRY_TIMES, ORG_CODE, AGENT_NO, PUBLIC_PASSWORD, IS_SEND, LAST_SEND_TIME, SELECT_SCOPE, SECOND_AGENT_ID, CHANGE_PASSWORD) VALUES (55555555, 1, '18888888888', 'TRUE', 'c4ca4238a0b923820dcc509a6f75849b', 0, null, 180, TO_DATE('2020-09-02 14:24:19', 'YYYY-MM-DD HH24:MI:SS'), '00:00:00', '23:59:59', 'SUPERADMIN', '管理员', TO_DATE('2020-09-02 14:24:19', 'YYYY-MM-DD HH24:MI:SS'), 'system', null, null, TO_DATE('2020-09-02 14:24:19', 'YYYY-MM-DD HH24:MI:SS'), null, null, '8625834091', null, 'Y', TO_DATE('2020-09-02 14:24:19', 'YYYY-MM-DD HH24:MI:SS'), 'WHOLE', null, null)")
    result = oral.select_data("select ID from posp_agent.operator where username='18888888888'")
    oral.close_db()
    assert result[0][0] == 55555555


def test_oracle_update():
    oral = OracleUtil('posp_agent')
    oral.execute_sql("update POSP_AGENT.OPERATOR set status='FALSE' where username='18888888888'")
    result = oral.select_data("select status from posp_agent.operator where username='18888888888'")
    oral.close_db()
    assert result[0][0] == 'FALSE'


def test_oracle_delete():
    oral = OracleUtil('posp_agent')
    oral.execute_sql("delete from POSP_AGENT.OPERATOR  where username='18888888888'")
    result = oral.select_data("select * from posp_agent.operator where username='18888888888'")
    oral.close_db()
    assert result == []
