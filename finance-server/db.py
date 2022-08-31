from flask_sqlalchemy import SQLAlchemy
import pymysql
from main import app
import datetime
import copy

pymysql.install_as_MySQLdb()

class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = 123456
    database = 'finance'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user,password,database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

db = SQLAlchemy(app)

class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    account = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    avatar_url = db.Column(db.String(128))

def addUser(account,username,password,avatar_url):
    user = User(account = account,username = username,password = password,avatar_url=avatar_url)
    db.session.add(user)
    db.session.commit()

def getUserByaccount(account):
    user = User.query.filter_by(account=account).first()
    print('user---------------',user)
    return user

def updateUserInfo(account,username,avatar_url):
    User.query.filter(User.account == account).update({'username':username,'avatar_url':avatar_url})
    db.session.commit()
    return True

def updateUserPassword(account,password):
    User.query.filter(User.account == account).update({'password':password})
    db.session.commit()
    return True

class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    account = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    file_url = db.Column(db.String(128))

def addRecord(account,file_url):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    record = Record(account=account,date=date,file_url=file_url)
    db.session.add(record)
    db.session.commit()

def getRecordByaccount(account):
    record = Record.query.filter_by(account=account).all()
    rec = []
    rk = {}
    index = 1
    for r in record:
        if(index%10==0):
            break
        rk['id'] = r.id
        rk['account'] = r.account
        rk['date'] = str(r.date)
        rk['file_url'] = r.file_url
        rec.append(copy.deepcopy(rk))
        index = index+1
    print(rec)
    return rec

def deleteRecordById(id):
    record = Record.query.filter_by(id=id).first()
    db.session.delete(record)
    db.session.commit()

if __name__ == '__main__':

    # # 删除所有表
    db.drop_all()

    # # 创建所有表
    db.create_all()
