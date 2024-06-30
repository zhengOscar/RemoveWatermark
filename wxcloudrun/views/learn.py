#coding=utf-8

from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response

from wxcloudrun import constant
from wxcloudrun import util
from flask import Response
import requests


@app.route("/api/menu", methods=['POST'])
def learn_menu():
    data = load_data('menu')
    return make_succ_response(data)
    
@app.route("/api/content", methods=['POST'])
def learn_data():
    
    # 获取请求体参数
    params = request.get_json()

    # 检查url参数
    if 'cat' not in params:
        return make_err_response('缺少参数')

    cat = params['cat']
    data = load_data(cat)
    if data==None:
        data=[]
    return make_succ_response(data)
    
@app.route("/api/l_adv", methods=['POST'])
def learn_adv():
    data ={
        'homeAdvId':'1',
        'detailAdvId':'1',
        'xdetailAdvId':'1',
        'settingAdvId':'1',
    }
    return make_succ_response(data)
    
def load_data(name):
    return util.import_module('data', "wxcloudrun.datas."+name);