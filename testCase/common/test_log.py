# -*- coding: UTF-8 -*-

"""
    @create：5/20/20 16:41
    @author：by aries
    @description：

"""

from common.logParameter import LogParameterSolution


# 测试点：日志样式输出
def test_log():
    LogParameterSolution().debug("---测试开始----")
    LogParameterSolution().info("操作步骤")
    LogParameterSolution().warning("----测试结束----")
    LogParameterSolution().error("----测试错误----")
