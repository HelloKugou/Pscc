#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

from pscc import QS, XS,Item, Parser, XPathParser, Spider


class Post(Item):
    title = QS('.title-content')

    async def save(self):
        print(self.title)


class MySpider(Spider):
    start_url = 'https://www.baidu.com/index.php?tn=monline_3_dg'
    concurrency = 5
    # headers = {'User-Agent': 'Google Spider'}
    parsers = [
               XPathParser('//span[@class="title-link"]/a/@href')
              ]


if __name__ == '__main__':
    MySpider.run()
