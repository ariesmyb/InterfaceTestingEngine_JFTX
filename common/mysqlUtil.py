# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-08 14:32
    @author: by aries
    @description: None
    
"""
import pymysql
from common.logParameter import LogParameterSolution
from params.dbConfig import *


class MysqlUtil:
    def __init__(self, host):
        user=mysql_dblist[host]["user"]
        passwd=mysql_dblist[host]["passwd"]
        self.db = pymysql.connect(host, user, passwd, port=3306, charset='utf8')
        self.cursor = self.db.cursor()
        self.log = LogParameterSolution()

    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            # 数据查询成功
            self.log().info('Query data succeeded!')
            return results
        except :
            # 数据查询异常
            self.log().error('Query data exception.')

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            # 操作成功
            self.log().info('The operation was successful!')
        except:
            self.db.rollback()
            # 操作异常，已回滚
            self.log().error('Exception, operation rolled back.')

    def close_db(self):
        self.cursor.close()
        self.db.close()
