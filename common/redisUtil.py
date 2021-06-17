# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-15 12:24
    @author: by aries
    @description: None
    
"""
import redis


class RedisUtil:
    def __init__(self):
        self.re = redis.StrictRedis(host='192.168.6.41', port=6379, db=1, decode_responses=True, password='online-redis')

    def set_redis(self, key, value):
        self.re.set(key, value)
        # print(self.re.get(key))

    def get_redis(self, key):
        return self.re.get(key)


if __name__ == '__main__':
    # RedisUtil().set_redis('NOT_STAND_MCC_LIMIT_AMOUNT_20200403','0')
    # print(RedisUtil().get_redis('NOT_STAND_MCC_LIMIT_AMOUNT_20200403'))
    # print(RedisUtil().get_redis('NOT_STAND_MCC_TRANS_AMOUNT_20200403'))
    codeLocal_FindPwd = RedisUtil().get_redis("AGENT_CHECK_CODE" + "17657020502")
    print(codeLocal_FindPwd)
