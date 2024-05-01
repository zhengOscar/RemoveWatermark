#coding=utf-8 
import util


def downLoad(url):
    #获取短连接码
    sub = "https://v.douyin.com/"+url.split("https://v.douyin.com/")[1].substring(0, 7);
    #通过短连接获取长链接
    redirectUrl = util.get_redirected_url(sub);
    return redirectUrl