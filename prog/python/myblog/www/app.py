# -*- encoding: utf-8 -*-

'''
@File    :   app.py
@Time    :   2019/05/11 16:16:44
@Author  :   YWB
@Version :   1.0
@Contact :   xxx@xxx.com
@License :   (C)Copyright 2017-2018
@Desc    :   MyBlog's main program

'''

# here put the import lib
import time
import json
import os
import asyncio
from aiohttp import web
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '0.0.0.0', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
