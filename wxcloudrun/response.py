import json

from flask import Response


def make_succ_empty_response():
    data = json.dumps({'code': 0, 'data': {}})
    return Response(data, mimetype='application/json')


def make_succ_response(param):
    if(isinstance(param, dict)):
        param['code']=0
    else:
        param = {'code': 0, 'data': param}
    data = json.dumps(param)
    return Response(data, mimetype='application/json')


def make_err_response(err_msg):
    data = json.dumps({'code': -1, 'errorMsg': err_msg})
    return Response(data, mimetype='application/json')
