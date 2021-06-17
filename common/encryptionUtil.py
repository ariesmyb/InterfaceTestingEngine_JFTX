# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 17:34
    @author：by aries
    @description：字符串md5加密

"""

import base64, hashlib, hmac
from common.logParameter import LogParameterSolution
from params.errorMessage import ErrorMessage


class EncryptionUtilSolution:
    def __init__(self):
        self.log = LogParameterSolution()
        self.key = b"86eb1492-6e08-481d-b377-678acd5c3de5"

    def md5_util(self, s=None):
        if s is None:
            self.log.error("s, None")
        else:
            if not isinstance(s, str):
                self.log.error("s, " + ErrorMessage().error_type)
        hashlib.md5().update(s.encode(encoding='utf-8'))
        return hashlib.md5().hexdigest()

    """
    Hmac算法可选以下多种算法
        MD5
        SHA1
        SHA256
        SHA384
        SHA512
    """
    def hmac_util(self, s=None, type="MD5"):
        return hmac.new(self.key, s.encode("utf-8"), type).hexdigest()

    def base64_util(self, body_str=None):
        return base64.b64encode(body_str.encode("utf-8"))

    def base64_util_decode(self, body_str=None):
        return base64.b64decode(body_str).decode("utf-8")
