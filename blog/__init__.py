#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/14 15:27
# @Author : iou
# @File   : __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from controller import blog_message
# from model import Category, User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lklzlwh@localhost:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#app.config.from_object('blog.setting')  # 模块下的setting.py文件名，不用加py后缀
#app.config.from_envvar('FLASKR_SETTINGS')  # 环境变量，指向配置文件setting的路径

db = SQLAlchemy(app)  # 创建数据库对象
from blog.controller import blog_message
