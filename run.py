#!/usr/bin/env python
# ecoding:utf8

import sys
reload (sys)
sys.setdefaultencoding('utf8')

"""
__author__ : zhy
__mtime__  :2017/12/24
"""

from flask import Flask , render_template,url_for,request,session,redirect
import config
from functools import wraps
import os
from exit import db
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.config['SECRET_KEY'] = os.urandom(24)
#上下文模型映射
# with app.app_context():
# 	db.create_all()

# 登录限制器

def login_required(func):
	@wraps(func)
	def dec_func(*args, **kwargs):
		if session.get('id'):
			return redirect(url_for('index'))
		else:
			return func(*args, **kwargs)	
	return 	dec_func	


@app.route('/')
def index():
	session['id'] = 'dadadadadad'
	return '这是我的第一个程序!'

@app.route('/get/')
@login_required
def get():
	return 'succee' 

#构子函数,路由跳转的时候就会执行的函数
@app.before_request
def my_before_request():
	print "hello word"

if __name__=='__main__':
	app.run()	
