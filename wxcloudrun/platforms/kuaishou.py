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
    
    vid=re.findall('https://www.douyin.com/video/(\w+)\?previous_page=app_code_link',redirectUrl)[0]
    redirectUrl=f'https://m.douyin.com/share/video/{vid}'
    #print(redirectUrl)
    resp = requests.get(url=redirectUrl, headers=headers)
     
    # 正则抓视频信息
    info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', resp.text)[0]
    #print(info)
     
    # url解码
    html_data = urllib.parse.unquote(info)
    #with open('b.txt', 'w',encoding='utf-8') as file:
    #    file.write(html_data)
    html_data = json.loads(html_data)
    video_url = html_data['app']['videoInfoRes']['item_list'][0]['video']['play_addr']['url_list'][0]
    video_url = video_url.replace("playwm","play")
    #print(video_url)
    return video_url