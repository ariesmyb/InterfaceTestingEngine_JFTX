# -*- coding: UTF-8 -*-

"""
    @create：5/27/20 10:11
    @author：by aries
    @description：

"""


class ToPathSolution:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return ToPathSolution('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
