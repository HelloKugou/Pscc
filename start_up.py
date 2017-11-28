#!/usr/bin/env python
#-*-coding:utf-8*-
# __all__=""
# __datetime__=""
# __purpose__="此脚本是用来直接启动所有的爬虫脚本"

import os
import subprocess


class Run:

    def __init__(self, dirname):
        self.dir = dirname

    """获取脚本集"""
    def get_py(self):
        pwd = os.getcwd()
        grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        """获得测试集"""
        crawler_test = os.path.join(grader_father, "Pscc", self.dir)
        for root, _, files in os.walk(crawler_test):
            test_list = [os.path.join(root, i) for i in files if i.endswith(".py") and not i.startswith("_")]
            return test_list

    """封装Popen"""
    def cmd(self,cmd):
        cmd = subprocess.Popen(cmd,shell=True,close_fds=True)
        cmd.wait()

    """执行每个脚本"""
    def run_cmd(self):
        task_cmd = ["python "+i for i in self.get_py()]
        for i in task_cmd:
            self.cmd(i)


if __name__ == "__main__":
    Run("test").run_cmd()

