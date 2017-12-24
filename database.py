# encoding:utf8

from exit import db

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	user = db.Column(db.String(30),nullable=False)
	password = db.Column(db.String(100),nullable=False)
	email = db.Column(db.String(80))