# -*- encoding: utf-8 -*-

'''
@File    :   reminder.py
@Time    :   2019/05/25 23:22:26
@Author  :   YWB
@Version :   1.0
@Contact :   xxx@xxx.com
@License :   (C)Copyright 2017-2018
@Desc    :   None

'''

# here put the import lib
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

# 在每分钟的31 - 33秒触发，每秒触发一次，每分钟触发3次
@scheduler.scheduled_job('cron', second='31-33')
def request_update_status():
    print('doing job...')


scheduler.start()
