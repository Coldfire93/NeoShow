#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/14 15:31
# @Author : iou
# @File   : setting.py
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#mysql数据库连接信息
SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3306/test"