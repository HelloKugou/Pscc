#!/usr/bin/env python
#-*-coding:utf-8*-
#日志记录模块

import logging
import logging.config
#获取配置文件
#使用方法
logging.config.fileConfig("../conf/logger.conf")
logger1 = logging.getLogger("root")
logger2 = logging.getLogger("example01")
logger3 = logging.getLogger("example02")
