# -*- coding: UTF-8 -*-

"""
    @create：5/21/20 14:47
    @author：by aries
    @description：生成随机数

"""

import random, datetime, time
from common.logParameter import LogParameterSolution
from params.errorMessage import ErrorMessage


class GetRandomNumberSolution:
    def __init__(self):
        self.log = LogParameterSolution()

    def get_random_number_4_dt(self, time_format="%Y%m%d%H%M%S%f"):
        return datetime.datetime.now().strftime(time_format)

    def get_random_year(self, yi=None):
        if yi is None:
            # 生成年
            y = random.randint(int(time.strftime('%Y')) - 50, int(time.strftime('%Y')) + 50)
        else:
            if not isinstance(yi, int):
                self.log.error("yi, " + ErrorMessage().error_type)
                return False
            y = yi
        return y

    def get_random_month(self, mi=None):
        if mi is None:
            # 生成月
            m = random.randint(1, 12)
        else:
            if not isinstance(mi, int):
                self.log.error("mi, " + ErrorMessage().error_type)
                return False
            if mi < 1 or mi > 12:
                self.log.error("mi, " + ErrorMessage().out_of_range)
                return False
            m = mi
        if m < 10:
            m = '0' + str(m)
            return m
        return m

    def get_random_day(self, yi=None, mi=None, di=None):
        for s in [self.get_random_year(yi=yi), self.get_random_month(mi=mi)]:
            if s is False:
                return False
        odd_month = [1, 3, 5, 7, 8, 10, 12]
        lesser_month = [4, 6, 9, 11]
        y = int(self.get_random_year(yi=yi))
        m = int(self.get_random_month(mi=mi))
        if di is None:
            # 生成日
            if m == 2:
                if (y % 4 == 0) & (y % 100 != 0) or y % 400 == 0:
                    d = random.randint(1, 29)
                else:
                    d = random.randint(1, 28)
            else:
                for x in odd_month:
                    if x == m:
                        d = random.randint(1, 31)
                for x in lesser_month:
                    if x == m:
                        d = random.randint(1, 30)
        else:
            if not isinstance(di, int):
                self.log.error("di, " + ErrorMessage().error_type)
                return False
            if m == 2:
                if (y % 4 == 0) & (y % 100 != 0) or y % 400 == 0:
                    if di < 1 or di > 29:
                        self.log.error("di, " + ErrorMessage().out_of_range)
                        return False
                else:
                    if di < 1 or di > 28:
                        self.log.error("di, " + ErrorMessage().out_of_range)
                        return False
            else:
                for x in odd_month:
                    if x == m:
                        if di < 1 or di > 31:
                            self.log.error("di, " + ErrorMessage().out_of_range)
                            return False
                for x in lesser_month:
                    if x == m:
                        if di < 1 or di > 29:
                            self.log.error("di, " + ErrorMessage().out_of_range)
                            return False

            d = di
        if d < 10:
            d = '0' + str(d)
            return d
        return d

    def get_phone_number(self, pni=None):
        if pni is None:
            return '1' + ''.join(random.sample('0123456789', 10))
        else:
            if not isinstance(pni, int):
                self.log.error("pi, " + ErrorMessage().error_type)
                return False
            if len(str(pni)) > 10 or pni < 0:
                self.log.error("pi, " + ErrorMessage().out_of_range)
                return False
            return '1' + str(pni) + ''.join(random.sample('0123456789', (10 - len(str(pni)))))
