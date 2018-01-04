#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="提供装饰器更好的使用python apimethod 方法"
from functools import wraps


class ApiMtehod:
    def __init__(self, method="GET"):
        self.method = method

    def __call__(self, cls):
        @wraps(cls)
        def wrap(*args, **kwargs):
            cc = cls.__dict__
            c = {i: cc[i] for i in cc if not i.startswith("__")}
            c["api_method"] = self.method
            Newcls = type(cls.__name__, (object,), c)
            print(Newcls.__dict__)
            return Newcls
        return wrap
