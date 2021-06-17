# -*- coding: UTF-8 -*-

"""
    @create：5/22/20 16:07
    @author：by aries
    @Description：

"""

import uuid
from common.logParameter import LogParameterSolution
from params.errorMessage import ErrorMessage


class StringUtilSolution:
    def __init__(self):
        self.log = LogParameterSolution()

    def is_chinese(self, s):
        if u'\u4e00' <= s <= u'\u9fff':
            return True
        return False

    def get_string_len(self, s):
        if not isinstance(s, str):
            self.log.error("s, " + ErrorMessage().error_type)
            return False
        n = 0
        for x in s:
            if self.is_chinese(x):
                n += 2
            else:
                n += 1
        return n

    def random_hex_string(self, hi=8):
        if not isinstance(hi, int):
            self.log.error("i, " + ErrorMessage().error_type)
            return False
        hs = str(uuid.uuid4()).replace('-', '')
        return hs[:hi].upper()

    def convert_string_2_hex(self, s):
        if not isinstance(s, str):
            self.log.error("s, " + ErrorMessage().error_type)
            return False
        hs = bytes(s, encoding="utf-8")
        return hs.hex()

    def convert_hex_2_string(self, hs):
        if not isinstance(hs, str):
            self.log.error("h, " + ErrorMessage().error_type)
            return False
        s = []
        for i in range(0, len(hs), 2):
            s.append(chr(int(hs[i:i+2], 16)))
        return ''.join(s)
