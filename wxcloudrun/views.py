from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response

from wxcloudrun import constant
from flask import Response
import requests

@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)
    
    
@app.route("/api/nocode", methods=['POST'])
def remove_watermark():
    # 获取请求体参数
    params = request.get_json()

    # 检查url参数
    if 'url' not in params:
        return make_err_response('缺少url参数')

    url = params['url']
    video_url=''
    platform=constant.check_platform(url);
    func=None
    if platform!=None :
        func = applyFunc("download",platform);
    
    if(None != func):
        video_url=func(url);
    else:
        return make_err_response('暂不支持该平台')
    
    return make_succ_response(video_url)


@app.route('/api/video', methods=['GET'])
def video_stream():
    # 获取请求体参数
    url = request.args.get('url')

    response = requests.get(url, stream=True)
    resp = Response(response.iter_content(), content_type='video/mp4')
    resp.headers=response.headers
    return resp


def applyFunc(functionName, channel):
    obj_module = __import__("wxcloudrun.platforms."+channel,fromlist=True)
    if hasattr(obj_module, functionName):
        return getattr(obj_module, functionName)
    return None