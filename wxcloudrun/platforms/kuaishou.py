#coding=utf-8
import requests
import re
import json

def download(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    
    #获取短连接码
    sub = re.findall('https://v.kuaishou.com/\w{6}', url)[0]
    #通过短连接获取长链接
    response = requests.get(sub, headers=headers,allow_redirects=False)
    videoUrl=''
    if response.status_code==301 or response.status_code==302 :
        videoUrl = response.headers['Location']
    
    #print(videoUrl)
    photoId=re.findall(r"https://v.m.chenzhongtech.com/fw/photo/(.*)\?.*",videoUrl)[0]
    url = 'https://www.kuaishou.com/graphql'
    #print(photoId)

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',  # 模拟浏览器访问
        "content-type": "application/json",  # 请求的参数类型为json数据
        "Cookie": "did=web_77f2054db30b4a4ca2a34875d7b12060; didv=1714906573000; kpf=PC_WEB; clientid=3; kpn=KUAISHOU_VISION",
        }
    data =json.dumps({"operationName": "visionVideoDetail",
            "variables": {"photoId": "%s"%(photoId), "page": "detail"},
            "query": "query visionVideoDetail($photoId: String, $type: String, $page: String, $webPageArea: String) {\n  "
                     "visionVideoDetail(photoId: $photoId, type: $type, page: $page, webPageArea: $webPageArea) {\n    "
                     "status\n    type\n    author {\n      id\n      name\n      following\n      headerUrl\n      "
                     "__typename\n    }\n    photo {\n      id\n      duration\n      caption\n      likeCount\n      "
                     "realLikeCount\n      coverUrl\n      photoUrl\n      liked\n      timestamp\n      expTag\n      "
                     "llsid\n      viewCount\n      videoRatio\n      stereoType\n      croppedPhotoUrl\n      manifest {"
                     "\n        mediaType\n        businessType\n        version\n        adaptationSet {\n          id\n "
                     "         duration\n          representation {\n            id\n            defaultSelect\n          "
                     "  backupUrl\n            codecs\n            url\n            height\n            width\n           "
                     " avgBitrate\n            maxBitrate\n            m3u8Slice\n            qualityType\n            "
                     "qualityLabel\n            frameRate\n            featureP2sp\n            hidden\n            "
                     "disableAdaptive\n            __typename\n          }\n          __typename\n        }\n        "
                     "__typename\n      }\n      __typename\n    }\n    tags {\n      type\n      name\n      "
                     "__typename\n    }\n    commentLimit {\n      canAddComment\n      __typename\n    }\n    llsid\n    "
                     "danmakuSwitch\n    __typename\n  }\n}\n"})  # 请求的data数据，json类型


    response = requests.post(url, headers=headers, data=data)
    
    #with open('b.txt', 'w',encoding='utf-8') as file:
    #   file.write(response.text)

    res = response.json()
    video_url = res['data']['visionVideoDetail']['photo']['photoUrl']

    return video_url