from main import app
from flask import request
import json
import os

from db import addUser,getUserByaccount,getRecordByaccount,addRecord,updateUserInfo,deleteRecordById,updateUserPassword

@app.route('/test',methods=['GET','POST'])
def test():
    s = {}
    print("-------------------------------------",os.path.join('/db/','as.csv'))
    s['data'] = 'ada'
    return json.dumps(s)


@app.route('/login',methods=['POST'])
def login():
    msg = {}
    if(request.method == 'POST'):
        # print(f"res:{request.args}")
        # x  = request.args.get('firstName')
        account = request.form['account']
        password = request.form['password']
        user = getUserByaccount(account)
        if(user.password!=password):
            msg['state'] = 'fail'
            msg['msg'] = '密码错误'
            return json.dumps(msg)
        elif(user.password == password):
            # user.pop('password')
            msg['info'] = {
                'id' : user.id,
                'account':user.account,
                'username':user.username,
                'avatar_url':user.avatar_url
            }
            msg['state'] = 'success'
        return json.dumps(msg)
    msg['state'] = 'fail'
    return json.dumps(msg)  


@app.route('/register',methods=['POST'])
def register():
    msg = {}
    if(request.method == 'POST'):
        # print(f"res:{request.args}")
        # x  = request.args.get('firstName')
        account = request.form['account']
        if(getUserByaccount(account)):
            msg['state'] = 'fail'
            msg['msg'] = '账号已存在'
            return json.dumps(msg)
        password = request.form['password']
        username = account
        if(account and password and username):
            addUser(account,username,password,'')
        user = getUserByaccount(account)
        msg['state'] = 'success'
        msg['info'] = {
            'id':user.id,
            'account':user.account,
            'username':user.username,
            'avatar_url':user.avatar_url
        }
        return json.dumps(msg)
    msg['state'] = 'fail'
    return json.dumps(msg)

@app.route('/updateinfo',methods=['POST'])
def update_info():
    msg = {}
    if(request.method == 'POST'):
        account = request.form['account']
        if(not getUserByaccount(account)):
            msg['state'] = 'fail'
            msg['msg'] = '异常状态，账号不存在'
            return json.dumps(msg)
        username = request.form['username']
        avatar_url = request.form['avatar_url']
        res = updateUserInfo(account,username,avatar_url)
        if(not res):
            msg['state'] = 'fail'
            msg['msg'] = '更新失败'
            return json.dumps(msg)
        user = getUserByaccount(account)
        msg['state'] = 'success'
        msg['info'] = {
            'id':user.id,
            'account':user.account,
            'username':user.username,
            'avatar_url':user.avatar_url
        }
        return json.dumps(msg)


@app.route('/getrecord',methods=['POST'])
def get_record():
    msg = {}
    if(request.method == 'POST'):
        account = request.form['account']
        record = getRecordByaccount(account)
        print("record",record)
        msg['state'] = 'success'
        msg['record'] = record
        return json.dumps(msg)
    msg['state'] = 'fail'
    return json.dumps(msg)

@app.route('/deleterecord',methods=['POST'])
def delete_record():
    msg = {}
    if(request.method == 'POST'):
        id = request.form['id']
        account = request.form['account']
        print('id',id)
        deleteRecordById(id)
        msg['state'] = 'success'
        record = getRecordByaccount(account)
        msg['record'] = record
        return json.dumps(msg)
    msg['state'] = 'fail'
    return json.dumps(msg)

# 弃用，貌似并不需要再额外加个api
@app.route('/setrecord',methods=['POST'])
def set_record():
    msg = {}
    if(request.method == 'POST'):
        account = request.form['account']
        file_url = request.form['file_url']
        addRecord(account,file_url)
        msg['state'] = 'success'
        return json.dumps(msg)
    msg['state'] = 'fail'
    msg['info'] = {
        'file_url':file_url
    }
    return json.dumps(msg)

# 修改密码
@app.route('/changepassword',methods=['POST'])
def change_password():
    msg = {}
    if(request.method == 'POST'):
        account = request.form['account']
        old_user = getUserByaccount(account)
        if(not old_user):
            msg['state'] = 'fail'
            msg['msg'] = '异常状态，账号不存在'
            return json.dumps(msg)
        old_password = request.form['old_password']
        if(old_user.password!=old_password):
            msg['state'] = 'fail'
            msg['msg'] = '初始密码错误'
            return json.dumps(msg) 
        new_password = request.form['new_password']
        res = updateUserPassword(account,new_password)
        if(not res):
            msg['state'] = 'fail'
            msg['msg'] = '更新失败'
            return json.dumps(msg)
        user = getUserByaccount(account)
        msg['state'] = 'success'
        msg['info'] = {
            'id':user.id,
            'account':user.account,
            'username':user.username,
            'avatar_url':user.avatar_url
        }
        return json.dumps(msg)
