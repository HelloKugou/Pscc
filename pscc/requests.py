#!/usr/bin/env python
#-*-coding:utf-8-*-

import asyncio
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except:
    pass

from utils.Logconfig import load_my_logging_cfg
logger = load_my_logging_cfg("")


async def fetch(url, spider, session, semaphore):
    with (await semaphore):
        try:
            if callable(spider.headers):
                headers = spider.headers()
            else:
                headers = spider.headers
            async with session.get(url, headers=headers, proxy=spider.proxy) as response:
                if response.status in [200, 201]:
                    data = await response.text()
                    return data
                logger.error('Error: {} {}'.format(url, response.status))
                return None
        except:
            pass
    return None