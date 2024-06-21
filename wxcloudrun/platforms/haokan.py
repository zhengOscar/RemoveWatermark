#coding=utf-8 
import requests
import re
import json

from wxcloudrun import util

def download(url):
    headers = {
        'User-Agent':util.android_user_agent
    }
    
    response = requests.get(url, headers=headers)
    info = re.findall('"clarityUrl":(.*?)],', response.text)[0]
    dic = json.loads(info+']')
    video_url =dic[0]['url']
    for item in dic:
        if( item['key']=='1080p'):
            video_url=item['url']
    
    #util.log_to_file('b.txt', response.text)
    download_url = video_url;
    return video_url,download_url