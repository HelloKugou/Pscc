# Pscc 一套真的“能用”的框架：smile
![](https://img.shields.io/badge/time-3day-red.svg)
![](https://img.shields.io/badge/build-passing-brightgreen.svg)

很多人去网上找项目总是苦于找不到，费劲，出于这个想法，我便结合现在的工作想开发一个基于python3的异步爬虫的框架，目前开发只有我自己一个，因此可能时间不太多，自己在其他方面也是一起在跟进，所以这个项目可以进度的不是很快，但每天保证都会更新！

PSC组织推出的Python3异步爬虫框架-Pscc，主要也是结合了aiohttp,asyncio,uvloop作一套主要的爬虫核心框架，整个框架还会涉及到数据库以及日常监控项，以及爬虫方面的爬取策略，完完全全可以在生产环境中使用，最重要的一点就是，完全异步！完全异步啊！ 
#大家都有什么建议，以及想要批评我的地方都快向我砸过来，提提issues,
#如果大家感觉我的这个爬虫想法还挺好，那就赶快来！

完整的功能是[master](https://github.com/PythonScientists/Pscc/tree/master)的分支，想要看最新的改动切换到[develop](https://github.com/PythonScientists/Pscc/tree/develop)分支就好。

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
#### 具体可以看下列图示


![启动图示](https://github.com/PythonScientists/Pscc/blob/master/help/start_up.png)


![错误启动图示](https://github.com/PythonScientists/Pscc/blob/master/help/start_up_error.png)


### 四-二  . 安装依赖

根据`Kenneth Reitz`的《Pyhon最佳实践》中构建虚拟环境的方式，初次尝试使用`Pipenv`这个工具来构建，进一步拓展还在探索中，这个库是基于`Virtualevn`库之上的，因此也是更佳简单使用,使用的时候直接在根目录下使用`pipenv install`即可，`pipenv`会自动寻找`pipfile`对里面的依赖进行下载

### 四-三  . 运行方式

由于项目是基于`pipenv`环境启动，在第二步安装完依赖之后，就可以启动项目，可以把爬虫脚本放置在默认的脚本目录当中，就是`test`目录，然后启动方式如下
`pipenv run python start_up.py --d test`,`start_up.py`为启动脚本，`--d`是选择启动目录

# 五 . 改进方向

###  虽然现在框架已经能够正常运行，但是相比于正常，使用的一般框架来说，还是会有很多不足的地方，希望大家能够多提意见，下面是各个模块的细节问题，将来也会按照下面来进行一些优化

- 1.**请求模块** （aiohttp框架来发送请求）

    - 1.细节一 代理问题（即将引入代理池） 
  
  
    - 2.细节二 消息头设置问题 （config文件配置）
    
    
    - 3.细节三 请求频率、请求间隔 （aiohttp和asyncio共同处理）
   
   
    - 4.细节四 返回html的编码问题 （解决utf-8和gbk）

- 2.**解析模块** （异步解析）

    - 1.细节一 解析深度设置 ()
  
  
    - 2.细节二 url管理 (即将使用rabbitmq)
    
    
    - 3.细节三 子域名拼接问题 (暂且手动配置)
  
  
    - 4.细节四 解析方式 （）

- 3.**数据定义模块**（）

    - 1.细节一 数据统计实现 （内置item统计）
    
  
    - 2.细节二 数据存储方式定义 （暂定console,文件,mysql）
    
 
- 4.**选择器模块** (目前支持三种选择器)

    - 1.细节一 选择器实现 (css,xpath,re)

- 5.**调度中心模块** （）

待完善

（额外定义的模块）

- 6.**中间间模块** ()

待完善

- 7.**存储模块** （）

    - 1.细节一 存储方式选择 
    
 
    - 2.细节二 存储方式标准化


- 8.**日志管理模块** ()

    - 1.细节一 何时使用日志 (根据logging模块改写)
    
 
    - 2.细节二 日志标准格式定义 （定义几种日志存储）
    
- 9.**工具模块** ()

    - 1.细节一 使用现有轮子 
    
 
    - 2.细节二 增加框架可用性 （插件形式增加框架结构、统计管理爬虫脚本文件、设置模块开关-自定义使用组件）
    
- 10.**插件模块** （）

    - 1.细节一 python实现插件系统
    
 
    - 2.细节二 强调拓展性，根据使用者的需要自动更改系统（热更新）

#  需要改进的点

- 1.不支持对https的协议


- 2.功能单一，不支持大规模爬取


- 3.不支持分布式爬取


- 4.组件实现简单、没有利用设计良好的轮子


# 继续开发模块中。。。

2017.12.02 改进启动模块，具体可看上面的[启动图示](####具体可以看下列图示)
2017.12.06 增加错误重试次数的限制
