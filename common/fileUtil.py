# -*- coding: UTF-8 -*-

"""
    @create：5/21/20 14:36
    @author：by aries
    @description：文件读、写、删等操作

"""

import os
from common.logParameter import LogParameterSolution
from params.errorMessage import ErrorMessage


class FileUtilSolution:
    def __init__(self):
        self.log = LogParameterSolution()

    def read_file(self, ps=None):
        if ps is None:
            self.log.error("ps, None")
        else:
            if not isinstance(ps, str):
                self.log.error("ps, " + ErrorMessage().error_type)
        try:
            with open(ps, 'r') as f:
                s = f.readlines()
            for i in range(0, len(s)):
                s[i] = s[i].rstrip('\n')
        except:
            self.log.error("File does not exist")
        return s

    def write_file(self, ps=None, ds=None):
        if ps is None:
            self.log.error("ps, None")
        else:
            if not isinstance(ps, str):
                self.log.error("ps, " + ErrorMessage().error_type)
        if ds is None:
            self.log.error("ds, None")

        with open(ps, 'a+') as f:
            f.write(ds)

    def del_file(self, ps=None):
        if ps is None:
            self.log.error("ps, None")
        else:
            if not isinstance(ps, str):
                self.log.error("ps, " + ErrorMessage().error_type)
        if os.path.exists(ps):
            os.remove(ps)
            return True
        self.log.error("File does not exist")
        return False

    def create_file_paths(self, ps=None):
        if ps is None:
            self.log.error("ps, None")
        else:
            if not isinstance(ps, str):
                self.log.error("ps, " + ErrorMessage().error_type)
        file_path = ps[0:ps.rfind("/")]

        if not os.path.exists(file_path):
            # 创建文件目录
            self.log.debug("Create file directory:" + file_path)
            os.makedirs(file_path)
        else:
            # 目录已存在
            self.log.debug("Directory already exists:" + file_path)

        if not os.path.exists(ps):
            # 创建文件
            self.log.debug("Create a file:" + ps)
            with open(ps, 'w+') as f:
                print(f.read())
        else:
            # 文件已存在
            self.log.debug("File already exist:" + ps)
