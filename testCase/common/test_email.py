# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 09:57
    @author：by aries
    @description：

"""

import os
from common.toPath import ToPathSolution
from common.emailUtil import EmailSolution
from params.emailVariable import EmailParams

report_file = os.path.join(str(ToPathSolution().Users.aries.Documents.GitHub.TestDemo.report), "report.html")


# 测试点：发送测试邮件
def test_send_mail():
    m = EmailSolution(
        username=EmailParams.from_addr,
        passwd=EmailParams.password,
        to_receiver=EmailParams.to_receiver,
        cc_receiver=EmailParams.cc_receiver,
        title='[接口/自动化测试]测试执行报告test',
        content="你好！<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;XXX接口/自动化测试执行结果，详见<font color=red>附件</font>。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;努力赚钱才是正经事，穷人的精力更多是在思考如何生活，富人才有精力享受生活。比如，她晚上邀你去她家做客，没钱的人或许会因为心疼打车钱而止步，有钱的人只会因为正在另一位姑娘家做客而拒绝。",
        ssl=True,
        file=report_file,
        )
    m.send_mail()
