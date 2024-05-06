#coding=utf-8 
import requests
import re
import json
from wxcloudrun.platforms import haokan

def download(url):

    return haokan.download(url)