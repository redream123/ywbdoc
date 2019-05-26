# -*- encoding: utf-8 -*-

"""
@File    :   autoStudy_CMA.py
@Time    :   2018/11/18 23:54:44
@Author  :   YWB
@Version :   1.0
@Contact :   xxx@xxx.com
@License :   (C)Copyright 2017-2018
@Desc    :   None

"""

# here put the import lib
from selenium import webdriver as wd

cmatc_url = "http://www.cmatc.cn/lms"
iedriver = r"C:\Program Files\Internet Explorer\IEDriverServer32.exe"

drv = wd.Ie(iedriver)
drv.get(cmatc_url)
drv.implicitly_wait(10)
drv.find_element_by_id("username").send_keys("770753")
drv.find_element_by_id("password").send_keys("123456")
drv.find_element_by_name("submit").click()
drv.get(
    "http://www.cmatc.cn/lms/app/lms/student/Userselectlesson/show.do?lessonId=112427"
)
# drv.find_element_by_css_selector("span.btn btn-success").click()
# drv.find_element_by_class_name("btn btn-success")
# 上述两种方式均未找到相应的span元素，未知原因。
drv.find_element_by_xpath('//span[@class="btn btn-success"]').click()
drv.close()
