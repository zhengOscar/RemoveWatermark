#coding=utf-8
import requests
from wxcloudrun.platforms import douyin


def download(url):
    return douyin.download(url)