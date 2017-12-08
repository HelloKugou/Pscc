#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __all__=""
# __datetime__="2017.12.08"
# __purpose__="构建插件系统"

"""
locals()->load plugin->locals()
"""
# 导入库
import os
import sys
# 优先级队列
from queue import PriorityQueue


class PluginSystem:
    """
    一个简单的插件系统，可以在指定目录下写插件脚本，并且方便导入
    插件列表实现方式为优先级队列，可以指定插件分数，限制导入

    """
    __slots__ = ("plugin_list", "_dir", "_score")

    def __init__(self):
        # 设置默认插件文件夹
        plugin_dir = os.path.join(os.getcwd(), "example")
        # 增加module模块搜索目录
        sys.path.append(plugin_dir)
        # 每个插件默认分数
        self._score = 0
        # 插件目录
        self._dir = plugin_dir
        self.plugin_list = PriorityQueue()

    @property
    def dir(self):
        """获取插件目录"""
        return self._dir

    @dir.setter
    def dir(self, value):
        """修改插件目录"""
        try:
            self._dir = value
        except Exception as e:
            print(e)

    @property
    def pl(self):
        return self.plugin_list

    @pl.setter
    def pl(self, indexvalue):
        """重构pl"""
        index, value = indexvalue
        try:
            name = self.plugin_list[index][1]
            self.plugin_list.pop(index)
            self.plugin_list.append((value, name))
        except AttributeError as e:
            print("没有注册插件，不能指定修改")
        return self.plugin_list

    def register(self, score=None):
        """
        :param score
        可选参数来限制插件列表
        :return list
        注册插件，返回插件列表(设计为一个优先级队列)
        """
        for _, _, i in os.walk(self._dir):
            for j in i:
                if j.endswith(".py"):
                    self.plugin_list.put((self._score, j))
        self.plugin_list = [self.plugin_list.get()
                            for _ in range(self.plugin_list.qsize())]
        # 根据得分限制插件
        if score:
            self.plugin_list = [i for i in self.plugin_list if i[0] >= score]
        return self.plugin_list

    def load_plugin(self):
        """
        :param
        :return:
        按照插件列表来加载插件
        """
        self.plugin_list = self.register()
        print("================开始加载===================\n"
              "'{}'文件夹下的{}个插件{}".format(
                        self._dir,
                        len(self.plugin_list),
                        self.plugin_list))
        for plugin in self.plugin_list:
            pluginm = __import__(list(plugin)[1].split(".")[0],
                                 globals(),
                                 locals())
            print("\n=============测试是否正确导入===============")
            print(sys.modules[list(plugin)[1].split(".")[0]])
            print("=============取值验证======================")
            try:
                print(pluginm.__name__)
                print("============导入成功并测试值成功=============\n")
            except ModuleNotFoundError as e:
                print("==========导入失败致测试失败================")

        print("\n==============加载完成=====================")

    def __getattr__(self, func):
        pass

    # def __repr__(self):
    #     print("PluginSystem-'{}'".format(self.dir))

    def __str__(self):
        """
        :return: str
        """
        strout = "PluginSystem-'{}'".format(self.dir)
        return str(strout)


if __name__ == "__main__":
    a = PluginSystem()
    # a.register(2)
    # a.load_plugin()
    # print(a.pl)
    # a.pl = (1, 1)
    # print(a.pl)
