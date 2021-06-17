# -*- coding: UTF-8 -*-

"""
    @create：2020-05-14 9:50
    @author：by aries
    @description：运行testCase全部测试脚本，生成测试报告，并发送邮件

"""

import os
from common.emailUtil import EmailSolution
from params.emailVariable import EmailParams

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))


def get_report_file(report_path):
    """ 获取最新的测试报告 """
    lists = os.listdir(report_path)
    # windows下用getmtime；mac下用getctime
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


if __name__ == "__main__":
    # 执行用例并生产报告
    os.system('pytest --html=./report/report.html --self-contained-html -v ./testCase/common')
    # 获取测试报告
    report_path = os.path.join(cur_path, "report")
    report_file = get_report_file(report_path)
    # 发送报告
    EmailSolution(
        username=EmailParams.from_addr,
        passwd=EmailParams.password,
        to_receiver=EmailParams.to_receiver,
        cc_receiver=EmailParams.cc_receiver,
        title='[接口/自动化测试]测试执行报告',
        content="你好！<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;XXX接口/自动化测试执行结果，详见<font color=red>附件</font>。",
        ssl=True,
        file=report_file,
    ).send_mail()
