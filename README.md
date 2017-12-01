# Pscc 一套真的“能用”的框架：smile
![](https://img.shields.io/badge/time-3day-red.svg)
![](https://img.shields.io/badge/build-passing-brightgreen.svg)

很多人去网上找项目总是苦于找不到，费劲，出于这个想法，我便结合现在的工作想开发一个基于python3的异步爬虫的框架，目前开发只有我自己一个，因此可能时间不太多，自己在其他方面也是一起在跟进，所以这个项目可以进度的不是很快，但每天保证都会更新！

PSC组织推出的Python3异步爬虫框架-Pscc，主要也是结合了aiohttp,asyncio,uvloop作一套主要的爬虫核心框架，整个框架还会涉及到数据库以及日常监控项，以及爬虫方面的爬取策略，完完全全可以在生产环境中使用，最重要的一点就是，完全异步！完全异步啊！ 
#大家都有什么建议，以及想要批评我的地方都快向我砸过来，提提issues,
#如果大家感觉我的这个爬虫想法还挺好，那就赶快来！

经过一周的努力，终于在空闲时间完成了这个爬虫的框架，目前阶段还是在测试框架的稳定性，测试好了之后会放上来

# 一 . 终极目标

### 必须快 - `python3的地基`

### 谁都可以用 - `框架出来的意义`

### 可定制化 - `一个让人满意的框架的最终目的`

# 二 . 构想架构

`主模块-存储模块-中间件管理模块-调度模块-请求模块`

# 三 . 已开发功能

- 1.请求部分（异步请求， 请求码规则过滤）
 
- 2.解析部分（css解析、正则解析、Xpath解析）

- 3.数据验证部分（）

- 4.存储部分（多种储存方式，）

# 四 . 了解框架

### 四-一 . 基本使用(也可以去[**test**](https://github.com/PythonScientists/Pscc/tree/master/test)目录下查看)，当然，为了方便，可以直接在test文件夹下放置爬虫脚本，由[**start_up.py**](https://github.com/PythonScientists/Pscc/blob/master/start_up.py)文件直接启动多个脚本

```
#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__="2017-11-28"
# __purpose__="基本使用"

"""引入基本包，受__all__限制"""
from pscc import XS, Item, XPathParser, Spider

"""构建子域名处理方法"""
class Title(Item):
    title = XS('//h1[@id="articleTitle"]')
    parsers = [
               XPathParser('//ul[@class="channel-newsGroup"][1]/li/a/@href', Title)
              ]


if __name__ == '__main__':
    #启动
    MySpider.run()
```

### 四-二  。安装依赖

根据Kenneth Reitz的Pyhon最佳实践中构建虚拟环境的方式，初次尝试使用Pipenv这个工具来构建，进一步拓展还在探索中，这个库是基于Virtualevn库之上的，因此也是更佳简单使用


# 五 . 改进方向

###  虽然现在框架已
