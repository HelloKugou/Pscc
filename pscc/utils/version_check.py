#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="版本检查"

import sys


def version_check():
    require = [3,6]
    flag = True
    now = (sys.version).split("|")[0]
    x,y = int(now.split(".")[0]), int(now.split(".")[1])
    if x >= require[0]:
        if y >= require[1]:
            pass
        else:
            print("minor error")
            flag = False
    else:
        print("major error")
        flag = False
    return flag