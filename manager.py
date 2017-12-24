# encoding:utf8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from run import app
from exit import db
from database import User

#模型-迁移文件-表(init migrate,upgrade)这三个命令
manager = Manager(app)
Migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ =='__main__':
	manager.run()
