# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-18 11:09
    @author: by aries
    @description: None
    
"""
import os.path

import jpype
from jpype import *


class JarUtil:
    jvmpath = jpype.getDefaultJVMPath()
    jvmArg = "-DyourProperty=yourValue "
    # jarpath=os.path.join(os.path.abspath('.'), 'D:/')
    jarpath = os.path.dirname(os.path.abspath(__file__))
    startJVM(jvmpath, "-ea", "-Djava.class.path=%s" % (jarpath + "/CommUtil.jar"))
    JDClass = JClass("com.ymhz.util.CommUtils")

    def to_hmac(self, data):
        key = '86eb1492-6e08-481d-b377-678acd5c3de5'
        Hmacmd5 = JarUtil.JDClass.toHmac(data, key)
        return Hmacmd5
        shutdownJVM()

    def seqencing(self, list):
        mp = java.util.HashMap()
        for item in list:
            for k in item.keys():
                mp.put(k, item.get(k))
        seqstr = JarUtil.JDClass.sortRequestParam(mp, True)
        return seqstr
        shutdownJVM()


if __name__ == '__main__':
    a = JarUtil().seqencing([{"admin": "1111"}, {"aaaaa": "2222"}, {"bbbbb": "3333"}, {"vvvvv": "4444"}])
    print(a)
    b = JarUtil().to_hmac(a)
    print(b)
