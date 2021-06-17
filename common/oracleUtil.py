# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-03 17:31
    @author: by aries
    @description: None
    
"""

import cx_Oracle

# cx_Oracle.init_oracle_client(lib_dir="/Users/martin/instantclient_19_3")
cx_Oracle.init_oracle_client(lib_dir=r"C:/Users/aries/instantclient_11_2")

from params.dbConfig import oracle_dblist
from common.logParameter import LogParameterSolution


class OracleUtil:
    # 创建数据库连接
    def __init__(self, dbname):
        connectifon = oracle_dblist[dbname]
        self.db = cx_Oracle.connect(connectifon)
        self.cursor = self.db.cursor()
        self.log = LogParameterSolution()

    # 查询数据
    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            # 数据查询异常
            self.log().error('Query data exception.')

    # 执行sql
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            # 操作异常，已回滚
            self.log().error('Exception, operation rolled back.')

    # 关闭数据库连接
    def close_db(self):
        self.cursor.close()
        self.db.close()
