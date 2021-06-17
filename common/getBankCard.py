# -*- coding: UTF-8 -*-

"""
    @create：2020-05-16 18:31
    @author：by aries
    @description：随机生成银行卡卡号

"""

import random, time
from params.bankNumber import debit_card_len_list, credit_card_len_list
from params.errorMessage import ErrorMessage
from common.logParameter import LogParameterSolution


class GetBankCardSolution:
    # bank_code_no = ''
    # card_bin = ''
    # tmp_bank_code_list = []

    def __init__(self):
        self.log = LogParameterSolution()

    def get_bank_card(self, card_type=None, card_bin=None, card_len=None):
        if card_type is not None:
            if card_type != 'debit' and card_type != 'credit':
                self.log.error("card_type, " + ErrorMessage().out_of_range)
                return False
            if card_type == 'debit':
                card_bin, card_len = random.choice(list(debit_card_len_list.items()))
            if card_type == 'credit':
                card_bin, card_len = random.choice(list(credit_card_len_list.items()))
        else:
            if card_bin is None:
                self.log.error("cardBin, None")
                return False
            else:
                if not isinstance(card_bin, str):
                    self.log.error("cardBin, " + ErrorMessage().error_type)
                    return False
                if len(card_bin) < 5 or len(card_bin) > 10:
                    self.log.error("cardBin, " + ErrorMessage().out_of_range)
                    return False
            if card_len is None:
                self.log.error("cardLen, None")
                return False
            else:
                if not isinstance(card_len, int):
                    self.log.error("cardLen, " + ErrorMessage().error_type)
                    return False
                if 15 > card_len or card_len > 20:
                    self.log.error("cardLen, " + ErrorMessage().out_of_range)
                    return False

        ran_timestamp = str(round(time.time()))
        if len(card_bin) != 6:
            card_len = card_len - len(card_bin) + 6
        bank_card = str(card_bin) + ran_timestamp[0:(card_len - 9)] + str(random.randint(10, 99))
        sum_odd = sum_even = 0
        count = 0
        for bank_card_value in bank_card[::-1]:
            if (count % 2) == 0:
                if int(bank_card_value) * 2 > 9:
                    sum_even += (int(bank_card_value) * 2 - 9)
                else:
                    sum_even += int(bank_card_value) * 2
            else:
                sum_odd += int(bank_card_value)
            count = count + 1
        if (sum_even + sum_odd) % 10 != 0:
            last_digit = 10 - (sum_even + sum_odd) % 10
        else:
            last_digit = 0
        bank_card = bank_card + str(last_digit)
        return bank_card
