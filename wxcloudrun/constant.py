



conf={
    'douyin':'https://v.douyin.com/',       #抖音
    'kuaishou':'https://v.kuaishou.com/',   #快手
    'huoshan':'https://share.huoshan.com',  #火山
    'pipix':'https://h5.pipix.com',         #皮皮虾
    'weishi':'https://isee.weishi.qq.com',  #微视
}

def check_platform(url):
    for key in conf:
        if conf[key] in url:
            return key
    return None