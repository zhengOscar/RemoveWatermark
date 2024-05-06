#coding=utf-8 
import requests
import re
import json

def download(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    info = re.findall('"clarityUrl":(.*?)],', response.text)[0]
    dic = json.loads(info+']')
    video_url =dic[0]['url']
    for item in dic:
        if( item['key']=='1080p'):
            video_url=item['url']
    #with open('b.txt', 'w',encoding='utf-8') as file:
    #   file.write(response.text)

    return video_url