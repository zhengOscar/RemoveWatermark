from datetime import datetime
from flask import render_template, request
from run import app
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
        video_url,download_url=func(url);
    else:
        return make_err_response('暂不支持该平台')
    
    data = {
        'video_url':video_url,
        'download_url':download_url
    }
    return make_succ_response(data)


@app.route('/api/video', methods=['GET'])
def video_stream():
    # 获取请求体参数
    url = request.args.get('url')

    response = requests.get(url, stream=True)
    resp = Response(response.iter_content(), content_type='video/mp4')
    resp.headers=response.headers
    return resp

@app.route("/api/adv", methods=['GET'])
def get_adv():
    adv={
        "index_adv_id":"",
        "video_adv_id":"",
        "my_adv_id":"",
        "reward_adv_id":"100",
    }
    return make_succ_response(adv)
    
@app.route("/api/login", methods=['POST'])
def login():
    # 获取请求体参数
    params = request.get_json()

    # 检查url参数
    if 'nikename' not in params:
        return make_err_response('缺少nikename参数')
    return make_succ_response("")
    

def applyFunc(functionName, channel):
    obj_module = __import__("wxcloudrun.platforms."+channel,fromlist=True)
    if hasattr(obj_module, functionName):
        return getattr(obj_module, functionName)
    return None