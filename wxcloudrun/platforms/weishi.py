#coding=utf-8
import requests
import re
import json
import urllib
from urllib import parse


def download(url):
    #获取短连接码
    sub = re.findall('https://v.douyin.com/\w{8}', url)[0]
    #通过短连接获取长链接
    redirectUrl = requests.get(sub, allow_redirects=True).url
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
    }
    
    
    video_url=''
    return video_url