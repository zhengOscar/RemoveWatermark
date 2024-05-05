#coding=utf-8
import requests
import re
import json
import urllib
from urllib import parse


def download(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
    }
    
    #获取短连接码
    sub = re.findall('https://v.kuaishou.com/\w{6}', url)[0]
    #通过短连接获取长链接
    response = requests.get(sub, headers=headers)
    
    with open('b.txt', 'w',encoding='utf-8') as file:
        file.write(response.text)
    #url = re.findall('src="(.*?)"', response.text)[0]
    #print(url);
    
    #redirectUrl = response.url;
    """
    with open('b.txt', 'w',encoding='utf-8') as file:
        file.write(response.text)
    #response = requests.get(url=redirectUrl, headers=headers)
    """
    
    """
    res = requests.get(url)
    total_size = round(int(res.headers["Content-Length"])/1024/1024)
    with open('vid.mp4', 'wb') as f:
        for chunk in tqdm(iterable=res.iter_content(1024*1024), total=total_size, unit='KB'):
            f.write(chunk)
    """
    video_url = ''
    return video_url