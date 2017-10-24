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

conn_dt = {"host":"127.0.0.1",
           "port":3306,
           "user":"linhanqiu",
           "password":"linhanqiu",
           "db":"shape"}
async def conn():
    pool = await aiomysql.create_pool(host=conn_dt.get("host"),
                                      port=conn_dt.get("port"),
                                      user=conn_dt.get("user"),
                                      password=conn_dt.get("password"),
                                      db=conn_dt.get("db"),
                                      loop=loop)
    async  with pool.acquire() as con:
        async with con.cursor() as cur:
            await cur.execute("select * from user limit 1")
            a = await cur.fetchone()
            print(a)
    pool.close()
    await pool.wait_closed()
loop.run_until_complete(conn())