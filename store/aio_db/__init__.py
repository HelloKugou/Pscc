#!/usr/bin/env python
#-*-coding:utf-8-*-
#使用uvloop代替asyncio的eventloop
import aiomysql
import asyncio

try:
    import uvloop
    loop = asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)
except:
    loop = asyncio.get_event_loop()

conn_dt = {"host":"192.168.0.202",
           "port":3306,
           "user":"suqi",
           "password":"123456",
           "db":"spider"}
import time
date = time.strftime("%Y-%m-%d",time.localtime())
import pandas as pd

async def conn():
    pool = await aiomysql.create_pool(host=conn_dt.get("host"),
                                      port=conn_dt.get("port"),
                                      user=conn_dt.get("user"),
                                      password=conn_dt.get("password"),
                                      db=conn_dt.get("db"),
                                      loop=loop)
    async  with pool.acquire() as con:
        async with con.cursor() as cur:
            await cur.execute("select source,count(*) as c from yd_new group by source")
            rd = await cur.fetchone()

    d = pd.DataFrame({
        "抓取来源":[],
        "数量":[]
    })
    t = ("数据来源","数量")
    rd = zip(t,rd)
    print(rd)
    pool.close()
    await pool.wait_closed()
loop.run_until_complete(conn())