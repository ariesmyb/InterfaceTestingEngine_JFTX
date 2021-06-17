# -*- coding: UTF-8 -*-

"""
    @create：2020-05-16 21:12
    @author：by aries
    @description：随机生成中文姓名、少数民族姓名

"""

import random
from common.logParameter import LogParameterSolution
from params.nameList import NameList


class GetChineseNameSolution:
    def __init__(self):
        self.log = LogParameterSolution()

    def gbk2312(self):
        h = random.randint(0xb0, 0xf7)
        b = random.randint(0xa1, 0xf9)
        val = f'{h:x}{b:x}'
        s = bytes.fromhex(val).decode('gb2312')
        return s

    def create_name(self):
        first_name = NameList.first_name_list[random.randint(0, len(NameList.first_name_list) - 1)]

        name = ''
        for i in range(random.randint(1, 2)):
            s = self.gbk2312()
            name = name + s

        return first_name + name

    def create_minority_name(self):
        minority_name = NameList.first_minority_name_list[random.randint(0, len(NameList.first_minority_name_list) - 1)]

        name = ''
        for i in range(random.randint(3, 6)):
            s = self.gbk2312()
            name = name + s

        return minority_name + "·" + name
