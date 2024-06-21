#coding=utf-8



def get_download_url(video_url):
    download_url = video_url
    
    split_str= '.douyinvod.com'
    datas = video_url.split(split_str)
    uri = 'https://v5-cold'
    
    if datas[0][:-1] == uri :
        download_url = "%s%s%s" % (uri, split_str, datas[1])
        
        

    return download_url;