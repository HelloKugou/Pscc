#!/usr/bin/env python
#-*-coding:utf-8-*-

from selector import Selector

class ItemType(type):
    def __new__(cls,name,bases,namespace):
        selectors={}
        namespace["_item_name"] = name
        namespace["_item_num"]  = 0
        for name,value in namespace.items():
            if isinstance(value,Selector):
                Selector[name] = value
        namespace["selectors"] = selectors
        for name in selectors:
            del namespace[name]
        return type.__new__(cls,name,bases,namespace)

    @property
    def name(self):
        return self._item_name

    @property
    def count(self):
        return self._item_count
"""
test
"""
item = ItemType("a",(1,2,3),{'a':1})
print(item)