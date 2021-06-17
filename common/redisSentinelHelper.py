# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-15 12:20
    @author: by aries
    @description: None
    
"""
from redis.sentinel import Sentinel


class RedisSentinelHelper:
    sentinel_list = [
        ('192.168.6.41', 6378),
        ('192.168.6.42', 6378),
        ('192.168.6.43', 6378)
    ]
    password = 'online-redis'
    service_name = 'mymaster'

    def __init__(self, sentinel_list, service_name, password, db):
        self.sentinel = Sentinel(sentinel_list, socket_timeout=0.5)
        self.service_name = service_name
        self.password = password
        self.db = db

    def get_master_redis(self):
        return self.sentinel.discover_master(self.service_name)

    def get_slave_redis(self):
        return self.sentinel.discover_slaves(self.service_name)

    def set_key(self, key, value):
        master = self.sentinel.master_for(
            service_name=self.service_name,
            socket_timeout=0.5,
            password=self.password,
            db=self.db
        )
        return master.set(key, value)

    def get_key(self, key):
        slave = self.sentinel.slave_for(
            service_name=self.service_name,
            socket_timeout=0.5,
            password=self.password,
            db=self.db
        )
        return slave.get(key)


def get_redis(key, db):
    rsh = RedisSentinelHelper(sentinel_list=RedisSentinelHelper.sentinel_list, password=RedisSentinelHelper.password,
                              service_name=RedisSentinelHelper.service_name, db=db)
    if rsh.get_key(key) is not None:
        return str(rsh.get_key(key), encoding='utf-8')
    else:
        return rsh.get_key(key)


def set_redis(key, value, db):
    rsh = RedisSentinelHelper(sentinel_list=RedisSentinelHelper.sentinel_list, password=RedisSentinelHelper.password,
                              service_name=RedisSentinelHelper.service_name, db=db)
    rsh.set_key(key, value)


if __name__ == '__main__':
    # set_redis('NOT_STAND_MCC_LIMIT_AMOUNT_20200403','100',3)
    # print(get_redis('NOT_STAND_MCC_LIMIT_AMOUNT_20200404',3))
    print(get_redis('AGENT_CHECK_CODE17657020502', 3))
