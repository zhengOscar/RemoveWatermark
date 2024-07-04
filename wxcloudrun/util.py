#coding=utf-8

import requests
import importlib

android_user_agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
window_user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'

# 获取字符串中指定字符  ---从字符串头开始
def get_mid_string(data, start, end):
    start_index = len(start)
    end_index = data.find(end, start_index)
    if end_index >= 0:
        return data[start_index:end_index]
    return data  

# 获取字符串中指定字符
def get_middle_string(data, start, end):
    start_index = data.find(start)
    if start_index >= 0:
        start_index += len(start)
        end_index = data.find(end, start_index)
        if end_index >= 0:
            return data[start_index:end_index]
    return data

#获取重定向地址    
def get_redirected_url(sub,headers=None, allow_redirects=True):
    response = requests.get(sub,headers=headers, allow_redirects=allow_redirects)
    url = response.url
    cookies = response.cookies
    if(allow_redirects==False):
        if response.status_code==301 or response.status_code==302 :
            url = response.headers['Location']
    return url,cookies
    
def log_to_file(file, data):
    with open(file, 'w',encoding='utf-8') as file:
        file.write(data)
        
def import_module(attr_name, module):
    obj_module = importlib.import_module(module)
    if hasattr(obj_module, attr_name):
        return getattr(obj_module, attr_name)
    return None
    
    
def find_node(data, node_path):
    _, res = h(data, node_path,0)

    if(_):
        return _,res;
    elif(is_dict(data)):
        for k in data:
            _,res = find_node(data[k], node_path)
            if(_):
                return _, res
        return False,None
    elif(is_array(data)):
        for v in data:
            _,res = find_node(v, node_path)
            if(_):
                return _, res
        return False,None
    else:
        return False,None
        
def h(data, node_path, index):
    node = node_path[index]
    if is_dict(data) and is_str( node_path[index] ):
        if( has_key(data, node) ):
            if (len(node_path)==index+1) :
                return True, data[node];
            return h(data[node], node_path, index+1)
        else :
            return False, None
    
    if is_array(data) and is_number(node_path[index]):
        if( len(data)>node ):
            if (len(node_path)==index+1) :
                return True, data[node]
            return h(data[node], node_path, index+1)
        else:
            return False, None
    
    return False,None
        
def has_key(obj, key):
    return key in obj;
        
def is_dict(obj):
    return isinstance(obj, dict)
    
    
def is_array(obj):
    return isinstance(obj, list);
    
def is_number(obj):
    return isinstance(obj, (int, float, complex))
    
def is_str(obj):
    return isinstance(obj, str);