#!/usr/bin/env python
#-*-coding:utf-8*-
# __all__=""
# __datetime__=""
# __purpose__="此脚本是用来直接启动所有的爬虫脚本"

import os
import subprocess
import click

class Run:
    """封装启动方法"""
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


@click.command()
@click.option("--d",default="test",help="指定爬虫脚本集")
def start_up(d):
    # 获取根目录下所有目录
    pwd = os.getcwd()
    root_dir = []
    for _, dirs, _ in os.walk(pwd):
        root_dir = dirs
        break

    # 查看输入项是否包含在其中
    if d in set(root_dir):
        """可选目录命令行启动方式"""
        click.secho(
            "----开始执行----\n"
            "--目录{}脚本--\n".format(d),
            bg="green",
            underline=True
        )
        Run(d).run_cmd()
        click.secho(
            "----执行结束----",
            bg="green",
            underline=True
        )
    else:
        req = input("是否创建'{}'目录:".format(d))
        if req not in ["y","n"]:
            click.secho(
                "您输入选项非法，请重新输入",
                bg="green",
                underline=True
            )
        elif req == "n":
            click.secho(
                "不执行任何操作，退出",
                bg="green",
                underline=True
            )
        elif req == "y":
            try:
                os.mkdir(d)
                click.secho(
                    "已创建'{}'目录，请放置爬虫脚本".format(d),
                    bg="green",
                    underline=True
                )
            except Exception as e:
                pass


if __name__ == "__main__":
    """更改爬虫脚本目录，启动程序"""
    start_up()
