# -*- coding: UTF-8 -*-

"""
    @create：5/18/20 13:49
    @author：by aries
    @description：日志输出文件或控制台输出

"""

import logging, colorlog, time, os
# 按文件大小滚动备份
from logging.handlers import RotatingFileHandler

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))

log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)
# 文件的命名
log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    # 'CRITICAL': 'red',
}


class LogParameterSolution:
    def __init__(self, log_name=log_name):
        self.log_name = log_name
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        # 使用RotatingFileHandler类，滚动备份日志
        fh = RotatingFileHandler(filename=self.log_name, mode='a', maxBytes=1024 * 1024 * 5, backupCount=5,
                                 encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler, 用于输出到控制台
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
