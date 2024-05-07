#coding=utf-8

import requests


android_user_agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
window_user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'

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
    
def get_redirected_url(sub,headers=None, allow_redirects=True):
    if(headers==None):
        response = requests.get(sub, allow_redirects)
    else:
        response = requests.get(sub,headers=headers, allow_redirects=allow_redirects)
    url = response.url

    if(allow_redirects==False):
        if response.status_code==301 or response.status_code==302 :
            url = response.headers['Location']
    return url
    
def log_to_file(file, data):
    with open(file, 'w',encoding='utf-8') as file:
        file.write(data)