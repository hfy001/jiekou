#coding:utf-8
import logging
from common import get_cwd
import os
import time
from logging.handlers import RotatingFileHandler


def get_log(logger_name):
    # 创建ogger输出日志对象
    logger = logging.getLogger(logger_name)
    # 设置最低日志级别：分别低到高有debug、info、warning、error以及critical
    logger.setLevel(level=logging.INFO)

    # 设置日志存放路径，日志文件名
    # 设置所有日志和错误日志的存放路径
    path = get_cwd.get_cwd()
    # 所有日志存放路径
    all_log_path1 = '../logs/ALL_Logs/'
    all_log_path = os.path.join(path, 'logs/ALL_Logs/')
    # 错误日志存放路径
    error_log_path = os.path.join(path, 'logs/Error_Logs/')
    # 设置日志文件名
    ctime = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    all_log_name = all_log_path + ctime + '.log'
    error_log_name = error_log_path + ctime + '.log'

    # 所有日志：:定义一个RotaingFileHandler，最多备份10个日志文件，每个日志文件最多1k
    all_handler = RotatingFileHandler(all_log_name, maxBytes=10 * 1024, backupCount=10)
    # 指定被处理的信息级别，低于设置级别的信息将被忽略
    all_handler.setLevel(logging.INFO)
    # 错误日志：:定义一个RotaingFileHandler，最多备份10个日志文件，每个日志文件最多1k。#另一种常用设置的级别日志放在指定文件里面#handler=logging.FileHandler("testlog1.txt")
    error_handler = RotatingFileHandler(error_log_name, maxBytes=10 * 1024, backupCount=10)
    # 指定被处理的信息级别，低于设置级别的信息将被忽略
    error_handler.setLevel(logging.DEBUG)
    # 创建一个handler输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 设置输出日志格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    error_log_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
    # 给handler添加输出的日志格式
    all_handler.setFormatter(all_log_formatter)
    error_handler.setFormatter(error_log_formatter)
    console_handler.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(all_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)
    return logger


logs=get_log("__name__")

# logs.info("111")