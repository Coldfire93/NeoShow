#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/14 15:41
# @Author : iou
# @File   : Category.py

# from blog import db
import sys

sys.path.append(r"H:\programming\NeoShow")
# sys.path.append("..")
import blog


class Category(blog.db.Model):
    __tablename__ = 'b_category'
    id = blog.db.Column(blog.db.Integer, primary_key=True)
    title = blog.db.Column(blog.db.String(50), unique=True)
    content = blog.db.Column(blog.db.String(100))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Category %r>' % self.title
