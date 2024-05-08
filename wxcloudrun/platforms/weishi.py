#coding=utf-8
import requests
import re
import json
import urllib
import random

from urllib import parse

from wxcloudrun import util

def download(url):
    headers = {
        'User-Agent':util.android_user_agent
    }
    #获取短连接码
    sub = re.findall('https://video.weishi.qq.com/\w{8}', url)[0]
    #通过短连接获取长链接
    redirect_url = util.get_redirected_url(sub,headers=headers, allow_redirects=False)
    #print(redirect_url)
    
    
    vid= redirect_url.split("&id=")[1][:17];
    random_time=random.random()
    play_url=f'https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage?t={random_time}&g_tk=&feedid={vid}&recommendtype=0&datalvl=&qua=&uin=&format=json&inCharset=utf-8&outCharset=utf-8'
    #print(play_url)

    response = requests.get(play_url)
    #util.log_to_file('b.txt', response.text)
    res = response.json()
    video_url=res['data']['feeds'][0]['video_url']
    return video_url