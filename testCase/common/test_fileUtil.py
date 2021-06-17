# -*- coding: UTF-8 -*-

"""
    @create：5/21/20 15:00
    @author：by aries
    @description：

"""

import os, pytest
from common.toPath import ToPathSolution
from common.fileUtil import FileUtilSolution

tps = os.path.join(str(ToPathSolution().Users.aries.Documents.GitHub.TestDemo.logs), "2020-06-03.log")


# 测试点：读取文件，并打印
@pytest.mark.run(order=3)
def test_read_file():
    tps = os.path.join(str(ToPathSolution().Users.aries.Documents.GitHub.TestDemo.logs), "2020-06-04.log")
    print(FileUtilSolution().read_file(ps=tps))


# 测试点：将tdata内容，写入文件
@pytest.mark.run(order=2)
def test_write_file():
    stata = "Rtr\ntest;\ncls"
    FileUtilSolution().write_file(ps=tps, ds=stata)


# 测试点：删除指定文件
@pytest.mark.run(order=4)
def test_del_file():
    assert FileUtilSolution().del_file(ps=tps) is True


# 测试点：删除指定文件失败
@pytest.mark.last
def test_del_file_false():
    assert FileUtilSolution().del_file(ps=tps) is False


# 测试点：在指定位置创建指定目录
@pytest.mark.run(order=1)
def test_create_file_paths():
    FileUtilSolution().create_file_paths(ps=tps)
