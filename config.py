#!/usr/bin/env python
#-*-coding:utf-8*-
# __all__=""
# __datetime__=""
# __purpose__=""

from utils.Error import (
                    NoKeyError
                        )


class Config:
    def __init__(self):
        pass

    """定义request的cfg"""

    class RequestCfg:
        request_dict = {
            "proxy": "127.0.0.1",
            "Rconcurrency": 100,
            "timeout": 100
        }

    """获取request的cfg"""
    def request(self,cfg):
        request_dict = self.RequestCfg().request_dict
        if request_dict.get(cfg):
            value = request_dict.get(cfg)
            return str(value)
        else:
            raise NoKeyError(cfg)


class DevConfig(Config):
    pass


class ProConfig(Config):
    pass


#test
# a = DevConfig()
# try:
#     print(type(a.request("timeout")))
# except NoKeyError as e:
#     print(e)
