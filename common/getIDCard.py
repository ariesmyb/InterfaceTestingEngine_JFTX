# -*- coding: UTF-8 -*-

"""
    @create：2020-05-16 20:11
    @author：by aries
    @description：随机生成身份证号

"""

import random
from common.getRandomNumber import GetRandomNumberSolution
from common.logParameter import LogParameterSolution
from params.districtCode import district_list
from params.errorMessage import ErrorMessage


class GetIDCardSolution:
    def __init__(self):
        self.log = LogParameterSolution()
        self.get_random_number = GetRandomNumberSolution()

    def regional_number(self, rni=None):
        if rni is None:
            """生成身份证前六位"""
            # 列表里面的都是一些地区的前六位号码
            rni = random.choice(list(district_list.values()))
            return rni
        else:
            if not isinstance(rni, int):
                self.log.error("rni, " + ErrorMessage().error_type)
                return False
            if len(str(rni)) != 6:
                self.log.error("rni, " + ErrorMessage().out_of_range)
                return False
            return rni

    def randoms_sex_number(self, rsni=None):
        randoms = ''
        if rsni is None:
            for i in range(3):
                randoms += str(random.randint(0, 9))
            return randoms
        else:
            if not isinstance(rsni, int):
                self.log.error("rsni, " + ErrorMessage().error_type)
                return False
            # si 取值范围：0-9，单数为：男，双数为：女
            if rsni < 0 or rsni > 9:
                self.log.error("rsni, " + ErrorMessage().out_of_range)
                return False
        for i in range(2):
            randoms += str(random.randint(0, 9))
        randoms += str(random.randrange(rsni, 9, 2))
        return randoms

    def get_id_card(self, rni=None, yi=None, mi=None, di=None, rsni=None):
        for s in [self.regional_number(rni=rni), self.get_random_number.get_random_year(yi=yi),
                  self.get_random_number.get_random_month(mi=mi), self.get_random_number.get_random_day(di=di),
                  self.randoms_sex_number(rsni=rsni)]:
            if s is False:
                return False
        id_card = str(self.regional_number(rni=rni)) + str(self.get_random_number.get_random_year(yi=yi)) + str(
            self.get_random_number.get_random_month(mi=mi)) + str(self.get_random_number.get_random_day(di=di)) + str(
            self.randoms_sex_number(rsni=rsni))
        wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        zip_wi_num_17 = zip(list(id_card), wi)
        s = sum(int(i) * j for i, j in zip_wi_num_17)
        y = s % 11
        id_card += check_code[y]
        return id_card
