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