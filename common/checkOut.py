# -*- coding: UTF-8 -*-

"""
    @create：2020-05-16 17:02
    @author：by aries
    @description：两个文件Md5(十六进制)值对比结果

"""

import hashlib
from common.logParameter import LogParameterSolution
from params.errorMessage import ErrorMessage


class CheckOutSolution:
    def __init__(self):
        self.log = LogParameterSolution()

    def check_file_md5(self, fs1=None, fs2=None):
        var1 = open(fs1, 'rb').read()
        var2 = open(fs2, 'rb').read()
        try:
            if hashlib.md5(var1).hexdigest() == hashlib.md5(var2).hexdigest():
                return True
            return False
        except:
            return False

    def check_bank_account(self, ns=None):
        if ns is None:
            self.log.error("ns, None")
            return False
        else:
            if not isinstance(ns, str):
                self.log.error("ns, " + ErrorMessage().error_type)
                return False
        count = 0
        # 奇数位，偶数位的和，初始值为0
        sum_odd = sum_even = 0
        for bank_code in ns[-2::-1]:
            if count % 2 == 0:
                # 偶数位的值×2。
                sum_even += (int(bank_code) * 2 - 9) if (int(bank_code) * 2 > 9) else int(bank_code) * 2
                count += 1
            else:
                # 奇数位的值直接相加。
                sum_odd += int(bank_code)
                count += 1
        # 正确的银行卡号，奇数位和偶数位的和，再加上验证位，必然能被 10 整除。
        if (sum_odd + sum_even + int(ns[-1:])) % 10 == 0:
            return True
        return False

    def embody(self, s=None, val=None):
        if s is None:
            self.log.error("s, None")
            return False
        else:
            if not isinstance(s, str):
                self.log.error("s, " + ErrorMessage().error_type)
                return False
        if val is None:
            self.log.error("val, None")
            return False
        else:
            if not isinstance(val, str):
                self.log.error("val, " + ErrorMessage().error_type)
                return False
        if s in val:
            return True
        self.log.info("Does not contain")
        return False
