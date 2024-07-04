#coding=utf-8
import requests
import re
import json
import urllib
from urllib import parse

from wxcloudrun import util
from wxcloudrun import url_util

def download(url):
    headers = {
        'User-Agent':util.android_user_agent
    }
    
    #获取短连接码
    sub = re.findall('https://v.douyin.com/\w{8}', url)[0]
    #通过短连接获取长链接
    #redirect_url,cookies = util.get_redirected_url(sub,headers=headers, allow_redirects=False)

    #vid=util.get_mid_string(redirect_url, 'https://www.iesdouyin.com/share/video/', '/?')
    #redirect_url=f'https://m.douyin.com/share/video/{vid}'
    #print(redirect_url)
    response = requests.get(url=sub, headers=headers)
    #util.log_to_file('b.txt', response.text)
    # 正则抓视频信息
    #info = re.findall('id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
    #print(info)
    
    info = re.findall('window._ROUTER_DATA = (.*?)</script>', response.text)[0];
    print(info);
     
    # url解码
    html_data = urllib.parse.unquote(info)    
    #util.log_to_file('b.txt', html_data)

    html_data = json.loads(html_data)
    #play_url = html_data['app']['videoInfoRes']['item_list'][0]['video']['play_addr']['url_list'][0]
    _,datas = util.find_node(html_data, ['video','play_addr','url_list'])
    play_url = datas[0]
    play_url = play_url.replace("playwm","play").replace('aweme.snssdk.com','www.iesdouyin.com');
    
    response.close();
    
    #获取实际播放地址
    video_url,cookies = util.get_redirected_url(play_url, allow_redirects=False)
    
    download_url = url_util.get_download_url(video_url);
    return video_url,download_url