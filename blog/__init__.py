#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/14 15:27
# @Author : iou
# @File   : __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from blog.controller import blog_message
from flask import request, render_template, flash, abort, url_for, redirect, session
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lklzlwh@localhost:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#app.config.from_object('blog.setting')  # 模块下的setting.py文件名，不用加py后缀
#app.config.from_envvar('FLASKR_SETTINGS')  # 环境变量，指向配置文件setting的路径

db = SQLAlchemy(app)  # 创建数据库对象

@app.route('/')
def show_entries():
    categorys = Category.query.all()
    return render_template('show_entries.html', entries=categorys)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    content = request.form['text']
    category = Category(title, content)
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=request.form['username']).first()
        passwd = User.query.filter_by(password=request.form['password']).first()

        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            #SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


class User(db.Model):
    __tablename__ = 'b_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Category(db.Model):
    __tablename__ = 'b_category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    content = db.Column(db.String(100))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Category %r>' % self.title
