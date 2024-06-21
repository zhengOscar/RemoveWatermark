#coding=utf-8
import requests
import re
import json
import urllib
from urllib import parse

from wxcloudrun import util

def download(url):
    headers = {
        'User-Agent':util.android_user_agent
    }
    #获取短连接码
    sub = re.findall('https://h5.pipix.com/s/\w{8}', url)[0]
    #通过短连接获取长链接
    redirect_url,cookies = util.get_redirected_url(sub,headers=headers, allow_redirects=False)
    #print(redirect_url)
    
    vid=util.get_mid_string(redirect_url, 'https://h5.pipix.com/item/', '?app_id')
    play_url=f'https://h5.pipix.com/bds/webapi/item/detail/?item_id={vid}&source=share'
    #print(play_url)

    response = requests.get(play_url)
    #util.log_to_file('b.txt', response.text)
    res = response.json()
    #print(res['data']['item']['video']['orgin_video_download']['url_list'][0]['url'])
    video_url=res['data']['item']['video']['video_download']['url_list'][0]['url']

    download_url = video_url;
    return video_url,download_url