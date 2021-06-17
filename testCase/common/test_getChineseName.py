# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 10:08
    @author：by aries
    @description：

"""

from common.getChineseName import GetChineseNameSolution


# 测试点：生成汉族中文姓名
def test_create_name():
    print(GetChineseNameSolution().create_name())


# 测试点：生成少数民族中文姓名
def test_create_minority_name():
    print(GetChineseNameSolution().create_minority_name())
