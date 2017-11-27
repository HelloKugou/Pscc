#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

from pscc import QS, XS,Item, Parser, XPathParser, Spider


class Post(Item):
    title = XS('//h1[@id="articleTitle"]')

    async def save(self):
        print(self.results)
        # pass

class MySpider(Spider):
    start_url = 'http://difang.gmw.cn/jl/node_12998.htm'
    concurrency = 5
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    parsers = [
               XPathParser('//ul[@class="channel-newsGroup"][1]/li/a/@href',Post)
              ]


if __name__ == '__main__':
    MySpider.run()
