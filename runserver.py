#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/14 15:27
# @Author : iou
# @File   : runserver.py
from blog import app

"""
@app.route('/')
def hello_world():
    return 'Hello,World. Yes!'
"""

if __name__ == '__main__':
    app.run()
